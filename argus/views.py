import discord
from discord import Embed, Interaction, ui

from argus.db.models.user import MemberModel
from argus.utils import update


class DebateVotingSelect(ui.View):
    def __init__(self, states, *args, **kwargs):
        self.states = states
        super().__init__(*args, **kwargs)

    @ui.select(
        placeholder="Select all that apply and click submit to vote.",
        options=[
            discord.SelectOption(
                label="Debater's arguments were factual.",
                value="Factual",
            ),
            discord.SelectOption(
                label="Debater's arguments were consistent or logically valid.",
                value="Consistent",
            ),
            discord.SelectOption(
                label="Debater observed the principle of charity.",
                value="Charitable",
            ),
            discord.SelectOption(
                label="Debater was respectful to others.",
                value="Respectful",
            ),
        ],
        min_values=0,
        max_values=4,
        custom_id='debate_vote_select',
    )
    async def on_select(self, interaction: Interaction, select: ui.Select):
        room = self.states["room"]
        author = self.states["author"]
        candidate = self.states["candidate"]
        result = room.match.vote(voter=author, candidate=candidate)

        if result is None:
            embed = Embed(
                title="Stance Not Set",
                description="You must set a stance for or against the topic.",
                color=0xE74C3C,
            )
            await update(interaction, embed=embed, ephemeral=True)
            return
        elif not result:
            embed = Embed(
                title="Invalid Candidate",
                description="You can only vote for debaters.",
                color=0xE74C3C,
            )
            await update(interaction, embed=embed, ephemeral=True)
            return

        candidate_data = await interaction.client.engine.find_one(
            MemberModel, MemberModel.member == candidate.id
        )
        if "Factual" in select.values:
            candidate_data.factual += 1
        if "Consistent" in select.values:
            candidate_data.consistent += 1
        if "Charitable" in select.values:
            candidate_data.charitable += 1
        if "Respectful" in select.values:
            candidate_data.respectful += 1

        candidate_data.vote_count += 1

        await interaction.client.engine.save(candidate_data)

        self.on_select.disabled = True
        await interaction.response.edit_message(view=self)

        embed = Embed(
            title="Vote Cast", description="Your vote has been cast", color=0x2ECC71
        )
        await update(interaction, embed=embed, ephemeral=True)
