import asyncio

import discord
from discord import app_commands, Embed, Permissions
from discord.ext import commands

from argus.checks import check_prerequisites_enabled
from argus.client import ArgusClient
from argus.constants import (
    DB_ROLE_NAME_MAP,
    ROLE_PERMISSIONS,
    RANK_RATING_MAP,
    ROLE_COLORS,
    DB_CHANNEL_NAME_MAP,
)
from argus.overwrites import generate_overwrites, NEGATIVE, MODERATION_BOT
from argus.utils import update


@app_commands.default_permissions(administrator=True)
class Setup(commands.GroupCog, name="setup"):
    def __init__(self, bot: ArgusClient) -> None:
        self.bot = bot
        super().__init__()

        # Setup Roles
        self.bot.state["map_roles"] = {
            "role_warden": None,
            "role_the_crown": None,
            "role_moderation_bot": None,
            "role_chancellor": None,
            "role_liege": None,
            "role_prime_minister": None,
            "role_minister": None,
            "role_host": None,
            "role_grandmaster": None,
            "role_legend": None,
            "role_master": None,
            "role_expert": None,
            "role_distinguished": None,
            "role_apprentice": None,
            "role_novice": None,
            "role_initiate": None,
            "role_rookie": None,
            "role_incompetent": None,
            "role_bot": None,
            "role_citizen": None,
            "role_events": None,
            "role_logs": None,
            "role_debate_ping": None,
            "role_detained": None,
            "role_everyone": None,
        }

        # Setup Channels
        self.bot.state["map_channels"] = {
            "category_information": None,
            "tc_rules": None,
            "tc_about": None,
            "tc_announcements": None,
            "tc_community_updates": None,
            "category_moderation": None,
            "tc_mod_commands": None,
            "tc_isolation": None,
            "category_interface": None,
            "tc_election_feed": None,
            "tc_debate_feed": None,
            "tc_commands": None,
            "category_events": None,
            "category_community": None,
            "tc_general": None,
            "tc_memes": None,
            "category_debate": None,
            "category_logs": None,
            "tc_moderator_actions": None,
            "tc_message_deletion": None,
            "tc_message_edits": None,
            "tc_ban_unban": None,
            "tc_nicknames": None,
            "tc_join_leave": None,
            "tc_automod": None,
            "tc_channels": None,
            "tc_invites": None,
            "tc_roles": None,
            "tc_voice": None,
        }

    @app_commands.command(
        name="roles",
        description="Setup roles required by the bot. This is a dangerous procedure that alters the database.",
    )
    @check_prerequisites_enabled()
    async def roles(self, interaction: discord.Interaction) -> None:
        await update(
            interaction,
            embed=Embed(
                title="Processing Roles",
                description="This may take a while.",
                color=0xF1C40F,
            ),
        )

        if self.bot.state["roles_are_setup"]:
            await update(
                interaction,
                embed=Embed(
                    title="Roles Already Set Up",
                    description="Please restart the bot manually if your still want to overwrite roles.",
                    color=0xE74C3C,
                ),
            )
            return

        # Delete All Roles
        for role in list(interaction.guild.roles)[1:]:
            if not role.managed:
                await role.delete(reason="Role Setup")
                await asyncio.sleep(5)

        # Ease of Access
        roles = self.bot.state["map_roles"]

        # Setup Basic Permissions
        roles["role_everyone"] = interaction.guild.default_role
        await roles["role_everyone"].edit(
            permissions=Permissions(permissions=2184252480)
        )

        # Setup Power Roles
        roles["role_warden"] = await interaction.guild.create_role(
            name="Warden",
            permissions=Permissions(permissions=8),
            colour=0xEB6A5C,
            hoist=False,
        )
        await interaction.guild.me.add_roles(roles["role_warden"])

        roles["role_the_crown"] = await interaction.guild.create_role(
            name="The Crown",
            colour=0xD4AF37,
            permissions=Permissions(permissions=0),
            hoist=False,
        )
        await interaction.guild.owner.add_roles(roles["role_the_crown"])

        roles["role_moderation_bot"] = await interaction.guild.create_role(
            name="Moderation Bot",
            permissions=Permissions(permissions=1089042513857),
            hoist=False,
        )

        roles["role_chancellor"] = await interaction.guild.create_role(
            name="Chancellor",
            colour=0x9B59B6,
            permissions=Permissions(permissions=1098639081441),
            hoist=False,
        )

        roles["role_liege"] = await interaction.guild.create_role(
            name="Liege",
            colour=0xE67E22,
            permissions=Permissions(permissions=1098639081409),
            hoist=False,
        )

        roles["role_prime_minister"] = await interaction.guild.create_role(
            name="Prime Minister",
            colour=0xE74C3C,
            permissions=Permissions(permissions=1097564815169),
            hoist=False,
        )

        roles["role_minister"] = await interaction.guild.create_role(
            name="Minister",
            colour=0x2ECC71,
            permissions=Permissions(permissions=1097564815169),
            hoist=False,
        )

        # Selective Permissions
        roles["role_host"] = await interaction.guild.create_role(
            name="Host", permissions=Permissions(permissions=0), hoist=False
        )

        # Event Roles
        roles["role_champion"] = await interaction.guild.create_role(
            name="Champion", permissions=Permissions(permissions=0), hoist=True
        )

        # Setup Rated Roles
        roles["role_grandmaster"] = await interaction.guild.create_role(
            name="Grandmaster", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_legend"] = await interaction.guild.create_role(
            name="Legend", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_master"] = await interaction.guild.create_role(
            name="Master", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_expert"] = await interaction.guild.create_role(
            name="Expert", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_distinguished"] = await interaction.guild.create_role(
            name="Distinguished", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_apprentice"] = await interaction.guild.create_role(
            name="Apprentice", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_novice"] = await interaction.guild.create_role(
            name="Novice", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_initiate"] = await interaction.guild.create_role(
            name="Initiate", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_rookie"] = await interaction.guild.create_role(
            name="Rookie", permissions=Permissions(permissions=0), hoist=True
        )

        roles["role_incompetent"] = await interaction.guild.create_role(
            name="Incompetent", permissions=Permissions(permissions=0), hoist=True
        )

        # Bot Roles
        roles["role_bot"] = await interaction.guild.create_role(
            name="Bot", permissions=Permissions(permissions=0), hoist=True
        )
        await interaction.guild.me.add_roles(roles["role_bot"])

        # Membership Roles
        roles["role_citizen"] = await interaction.guild.create_role(
            name="Citizen", permissions=Permissions(permissions=2251673153), hoist=False
        )

        # Optional Roles
        roles["role_logs"] = await interaction.guild.create_role(
            name="Logs", permissions=Permissions(permissions=0), hoist=False
        )

        roles["role_events"] = await interaction.guild.create_role(
            name="Events", permissions=Permissions(permissions=0), hoist=False
        )

        roles["role_debate_ping"] = await interaction.guild.create_role(
            name="Debate Ping", permissions=Permissions(permissions=0), hoist=False
        )

        # Punishment Roles
        roles["role_detained"] = await interaction.guild.create_role(
            name="Detained", permissions=Permissions(permissions=0), hoist=False
        )

        # Update Database
        await self.bot.db.upsert(
            interaction.guild,
            role_warden=roles["role_warden"].id,
            role_the_crown=roles["role_the_crown"].id,
            role_moderation_bot=roles["role_moderation_bot"].id,
            role_chancellor=roles["role_chancellor"].id,
            role_liege=roles["role_liege"].id,
            role_prime_minister=roles["role_prime_minister"].id,
            role_minister=roles["role_minister"].id,
            role_host=roles["role_host"].id,
            role_champion=roles["role_champion"].id,
            role_grandmaster=roles["role_grandmaster"].id,
            role_legend=roles["role_legend"].id,
            role_master=roles["role_master"].id,
            role_expert=roles["role_expert"].id,
            role_distinguished=roles["role_distinguished"].id,
            role_apprentice=roles["role_apprentice"].id,
            role_novice=roles["role_novice"].id,
            role_initiate=roles["role_initiate"].id,
            role_rookie=roles["role_rookie"].id,
            role_incompetent=roles["role_incompetent"].id,
            role_bot=roles["role_bot"].id,
            role_citizen=roles["role_citizen"].id,
            role_member=roles["role_member"].id,
            role_events=roles["role_events"].id,
            role_logs=roles["role_logs"].id,
            role_debate_ping=roles["role_debate_ping"].id,
            role_detained=roles["role_detained"].id,
        )

        # Update State
        self.bot.state["roles_are_setup"] = True

        # Send Confirmation Message
        await update(
            interaction,
            embed=Embed(
                title="Roles Updated",
                description="Roles have been successfully set up.",
                color=0x2ECC71,
            ),
        )

    async def check_roles_exist(self, interaction: discord.Interaction) -> bool:
        guild = self.bot.get_guild(self.bot.config["global"]["guild_id"])

        # Setup Role Cache
        for role in guild.roles:
            if not role.managed:
                self.bot.state["map_roles"][DB_ROLE_NAME_MAP[role.name]] = role

        # Check Roles Exist in Database
        for role in guild.roles[1:]:
            if not role.managed:
                db_role_id = await self.bot.db.get(
                    guild, state=f"{DB_ROLE_NAME_MAP[role.name]}"
                )
                if not db_role_id:
                    await update(
                        interaction,
                        embed=Embed(
                            title=f"Roles Missing",
                            description="Please run the setup of roles again. "
                            "Roles in this server were never added to the database",
                            color=0xE74C3C,
                        ),
                        ephemeral=True,
                    )
                    return False
                elif role.id == db_role_id:
                    continue
                else:
                    await update(
                        interaction,
                        embed=Embed(
                            title=f"Data Mismatch",
                            description="Please run the setup of roles again. "
                            "Roles in the server do not match the database.",
                            color=0xE74C3C,
                        ),
                        ephemeral=True,
                    )
                    return False
        return True

    @app_commands.command(
        name="channels",
        description="Setup channels required by the bot. This is a dangerous procedure that alters the database.",
    )
    async def channels(self, interaction: discord.Interaction) -> None:
        await update(
            interaction,
            embed=Embed(
                title="Processing Channels",
                description="This may take a while.",
                color=0xF1C40F,
            ),
        )

        if interaction.channel != interaction.guild.rules_channel:
            await update(
                interaction,
                embed=Embed(
                    title="Incorrect Channel",
                    description="This command cannot be run in this channel.",
                    color=0xE74C3C,
                ),
                ephemeral=True,
            )
            return

        roles_exist = await self.check_roles_exist(interaction)

        if not roles_exist:
            await update(
                interaction,
                embed=Embed(
                    title="Data Mismatch",
                    description="Please run the setup of roles again. "
                    "Roles in the server do not match the database.",
                    color=0xE74C3C,
                ),
            )
            return

        # Shortcuts
        guild = interaction.guild
        roles = self.bot.state["map_roles"]
        channels = self.bot.state["map_channels"]

        # Delete All Channels
        skipped_channels = [guild.rules_channel, guild.public_updates_channel]
        for channel in guild.channels:
            if channel not in skipped_channels:
                await channel.delete()

        # Setup Information Category
        channels["category_information"] = await guild.create_category_channel(
            name="Information",
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="information"
            ),
        )

        await guild.rules_channel.edit(
            category=channels["category_information"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="information"
            ),
        )
        channels["tc_rules"] = guild.rules_channel

        channels["tc_about"] = await guild.create_text_channel(
            name="about",
            category=channels["category_information"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="information"
            ),
        )

        channels["tc_announcements"] = await guild.create_text_channel(
            name="announcements",
            category=channels["category_information"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="announcements"
            ),
        )

        await guild.public_updates_channel.edit(
            category=channels["category_information"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="community-updates"
            ),
        )
        channels["tc_community_updates"] = guild.rules_channel

        # Set Positions for Information Category
        await guild.rules_channel.edit(position=2)
        await channels["tc_about"].edit(position=3)
        await channels["tc_announcements"].edit(position=4)
        await guild.public_updates_channel.edit(position=5)

        # Setup Moderation Category
        channels["category_moderation"] = await guild.create_category_channel(
            name="Moderation",
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="moderation"
            ),
        )

        channels["tc_mod_commands"] = await guild.create_text_channel(
            name="mod-commands",
            category=channels["category_moderation"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="moderation"
            ),
        )

        channels["tc_isolation"] = await guild.create_text_channel(
            name="isolation",
            category=channels["category_moderation"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="isolation"
            ),
        )

        # Setup Interface Category
        channels["category_interface"] = await guild.create_category_channel(
            name="Interface",
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="interface"
            ),
        )

        channels["tc_election_feed"] = await guild.create_text_channel(
            name="election-feed",
            category=channels["category_interface"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="interface"
            ),
        )

        channels["tc_debate_feed"] = await guild.create_text_channel(
            name="debate-feed",
            category=channels["category_interface"],
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="interface"
            ),
        )

        channels["tc_commands"] = await guild.create_text_channel(
            name="commands",
            category=channels["category_interface"],
            slowmode_delay=5,
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="commands"
            ),
        )

        # Setup Events Category
        channels["category_events"] = await guild.create_category_channel(
            name="Events",
            overwrites=generate_overwrites(interaction, roles=roles, channel="events"),
        )

        # Setup Community Category
        channels["category_community"] = await guild.create_category_channel(
            name="Community",
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="community"
            ),
        )

        channels["tc_general"] = await guild.create_text_channel(
            name="general",
            category=channels["category_community"],
            slowmode_delay=5,
            overwrites=generate_overwrites(interaction, roles=roles, channel="general"),
        )

        channels["tc_memes"] = await guild.create_text_channel(
            name="memes",
            category=channels["category_community"],
            slowmode_delay=5,
            overwrites=generate_overwrites(
                interaction, roles=roles, channel="community"
            ),
        )

        # Setup Debate Category
        channels["category_debate"] = await guild.create_category_channel(
            name="Debate",
            overwrites=generate_overwrites(interaction, roles=roles, channel="debate"),
        )

        # Setup Logs Category
        channels["category_logs"] = await guild.create_category_channel(
            name="Logs",
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_moderator_actions"] = await guild.create_text_channel(
            name="moderator-actions",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_message_deletion"] = await guild.create_text_channel(
            name="message-deletion",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_message_edits"] = await guild.create_text_channel(
            name="message-edits",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_ban_unban"] = await guild.create_text_channel(
            name="ban-unban",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_nicknames"] = await guild.create_text_channel(
            name="nicknames",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_join_leave"] = await guild.create_text_channel(
            name="join-leave",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_automod"] = await guild.create_text_channel(
            name="automod",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_channels"] = await guild.create_text_channel(
            name="channels",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_invites"] = await guild.create_text_channel(
            name="invites",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_roles"] = await guild.create_text_channel(
            name="roles",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        channels["tc_voice"] = await guild.create_text_channel(
            name="voice",
            category=channels["category_logs"],
            overwrites=generate_overwrites(interaction, roles=roles, channel="logs"),
        )

        # Create Debate Channels
        for _channel_number in range(1, 21):
            channels[f"vc_debate_{_channel_number}"] = await guild.create_voice_channel(
                name=f"Debate {_channel_number}",
                category=channels["category_debate"],
                overwrites=generate_overwrites(
                    interaction, roles=roles, channel="debate"
                ),
            )

            if _channel_number != 1:
                await channels[f"vc_debate_{_channel_number}"].edit(
                    overwrites={
                        roles["role_moderation_bot"]: MODERATION_BOT,
                        roles["role_citizen"]: NEGATIVE,
                        roles["role_member"]: NEGATIVE,
                        roles["role_everyone"]: NEGATIVE,
                    }
                )

            _channel_ids = {
                f"vc_debate_{_channel_number}": channels[
                    f"vc_debate_{_channel_number}"
                ].id,
            }
            await self.bot.db.upsert(guild, **_channel_ids)

        # Update Database
        _database_entries = {
            db_entry: channels[db_entry].id for db_entry in DB_CHANNEL_NAME_MAP.values()
        }
        await self.bot.db.upsert(guild, **_database_entries)

        # Send Confirmation Message
        await update(
            interaction,
            embed=Embed(
                title="Channels Updated",
                description="Channels have been successfully set up.",
                color=0x2ECC71,
            ),
        )


@app_commands.default_permissions(administrator=True)
class Migrate(commands.GroupCog, name="migrate"):
    def __init__(self, bot: ArgusClient) -> None:
        self.bot = bot
        super().__init__()

    @app_commands.command(
        name="roles",
        description="Add and remove roles required by the bot. This is a dangerous procedure that modifies the server.",
    )
    @check_prerequisites_enabled()
    async def roles(self, interaction: discord.Interaction) -> None:
        guild = self.bot.get_guild(self.bot.config["global"]["guild_id"])

        await update(
            interaction,
            embed=Embed(
                title="Migrating Roles",
                description="This may take a while.",
                color=0xF1C40F,
            ),
        )

        # Check if role exist and that their permissions are correct.
        # If incorrect fix it automatically.
        for role in guild.roles:
            if not role.managed:
                if role.name in DB_ROLE_NAME_MAP.keys():
                    if (
                        role.permissions.value
                        == ROLE_PERMISSIONS[DB_ROLE_NAME_MAP[role.name]]
                    ):
                        if ROLE_COLORS[DB_ROLE_NAME_MAP[role.name]]:
                            if (
                                role.color.value
                                == ROLE_COLORS[DB_ROLE_NAME_MAP[role.name]]
                            ):
                                continue
                            else:
                                await role.edit(
                                    color=ROLE_COLORS[DB_ROLE_NAME_MAP[role.name]]
                                )
                        else:
                            continue
                    else:
                        await role.edit(
                            permissions=Permissions(
                                ROLE_PERMISSIONS[DB_ROLE_NAME_MAP[role.name]]
                            )
                        )
                else:
                    await role.delete()

        db_roles = list(DB_ROLE_NAME_MAP.keys())
        db_roles.remove("@everyone")
        for db_role_name in db_roles:
            role = discord.utils.get(guild.roles, name=db_role_name)
            if ROLE_COLORS[DB_ROLE_NAME_MAP[db_role_name]]:
                if not role:
                    await guild.create_role(
                        name=db_role_name,
                        permissions=Permissions(
                            ROLE_PERMISSIONS[DB_ROLE_NAME_MAP[db_role_name]]
                        ),
                        color=ROLE_COLORS[DB_ROLE_NAME_MAP[db_role_name]],
                        hoist=bool(DB_ROLE_NAME_MAP[db_role_name] in RANK_RATING_MAP),
                    )
            else:
                if not role:
                    await guild.create_role(
                        name=db_role_name,
                        permissions=Permissions(
                            ROLE_PERMISSIONS[DB_ROLE_NAME_MAP[db_role_name]]
                        ),
                        hoist=bool(DB_ROLE_NAME_MAP[db_role_name] in RANK_RATING_MAP),
                    )

        current_positions = {}
        for role in guild.roles:
            current_positions[role.name] = role.position

        positions = {guild.me.top_role: 1}
        db_role_names = {
            _: DB_ROLE_NAME_MAP[_] for _ in DB_ROLE_NAME_MAP if _ != "@everyone"
        }
        for index, db_role_name in enumerate(db_role_names):
            role = discord.utils.get(guild.roles, name=db_role_name)
            positions[role] = index + 2

        managed_roles = []
        for role in guild.roles:
            if role.managed and not role.is_default():
                if role != guild.me.top_role:
                    managed_roles.append(role)

        for index, role in enumerate(managed_roles):
            positions[role] = len(positions) + index + 1

        keys = list(positions.keys())
        values = list(positions.values())[::-1]
        positions = dict(zip(keys, values))
        await guild.edit_role_positions(positions)

        # Prime Local Cache
        roles = {}
        for role in guild.roles:
            if not role.managed and not role.is_default():
                roles[DB_ROLE_NAME_MAP[role.name]] = role

        # Assign Roles
        await guild.owner.add_roles(roles["role_the_crown"])

        # Hoist Roles
        await roles["role_champion"].edit(hoist=True)

        # Update Database
        await self.bot.db.upsert(
            interaction.guild,
            role_warden=roles["role_warden"].id,
            role_the_crown=roles["role_the_crown"].id,
            role_moderation_bot=roles["role_moderation_bot"].id,
            role_chancellor=roles["role_chancellor"].id,
            role_liege=roles["role_liege"].id,
            role_prime_minister=roles["role_prime_minister"].id,
            role_minister=roles["role_minister"].id,
            role_host=roles["role_host"].id,
            role_champion=roles["role_champion"].id,
            role_grandmaster=roles["role_grandmaster"].id,
            role_legend=roles["role_legend"].id,
            role_master=roles["role_master"].id,
            role_expert=roles["role_expert"].id,
            role_distinguished=roles["role_distinguished"].id,
            role_apprentice=roles["role_apprentice"].id,
            role_novice=roles["role_novice"].id,
            role_initiate=roles["role_initiate"].id,
            role_rookie=roles["role_rookie"].id,
            role_incompetent=roles["role_incompetent"].id,
            role_bot=roles["role_bot"].id,
            role_citizen=roles["role_citizen"].id,
            role_member=roles["role_member"].id,
            role_events=roles["role_events"].id,
            role_logs=roles["role_logs"].id,
            role_debate_ping=roles["role_debate_ping"].id,
            role_detained=roles["role_detained"].id,
        )

        # Send Confirmation Message
        await update(
            interaction,
            embed=Embed(
                title="Roles Migrated",
                description="Missing roles and their permissions have been set up.",
                color=0x2ECC71,
            ),
        )


async def setup(bot: ArgusClient) -> None:
    await bot.add_cog(
        Setup(bot), guilds=[discord.Object(id=bot.config["global"]["guild_id"])]
    )
    await bot.add_cog(
        Migrate(bot), guilds=[discord.Object(id=bot.config["global"]["guild_id"])]
    )
