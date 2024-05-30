<div style="text-align: center;">
<img src="resources/images/Argus Badge.png" alt="drawing" style="width:100%;"/>
</div>

<br>

<b>Disclaimer: Project <u>Not Maintained</u></b>

Setting up this bot is easy. Invite the bot account to your server first. Then keep note of the guild `id`.
Make sure the server is empty and has the community option enabled. You also have to give the bot admin and the highest role in the server (if you invited the bot with admin permission, drag the role to the top).

Finally make sure you set a rules channel named "rules" and a community updates channel called "community-updates".

Now we can truly begin.

## Creating the discord bot account

First of all, you have to create an account for your Discord bot.
This can be done at the following link: https://discord.com/developers/applications

A detailed guide how to do this and obtain the bot token (which is needed for the next step) is available here:
https://discordpy.readthedocs.io/en/latest/discord.html

Also make sure to enable the privileged gateway intents in the bot tab like so:
![discord_bot_intents.png](resources/discord_bot_intents.png)

## Creating a MongoDB database

1. Create an account at https://www.mongodb.com/cloud/atlas/register
2. Once that's done, you should be prompted to deploy your cluster like on the image below. Select the M0 free tier, give your cluster a name, select the provider and region, then press "Create Deployment"
![mongodb_deploy_cluster.png](resources/mongodb_deploy_cluster.png)
3. Next, choose a username and password for the database user and press "Create Database User"
![mongodb_create_database_user.png](resources/mongodb_create_database_user.png)
4. Press on "Choose a connection method" -> "Drivers" and copy the link starting with "mongodb+srv://", make sure to replace the "<password>" with the actual password you set for the database user in the previous step
![mongodb_connection_string.png](resources/mongodb_connection_string.png)
5. Once that's done, head into the "Network Access" tab in the "Security" category on the left side of your screen, then press "ADD IP ADDRESS" on the right side, choose "ALLOW ACCESS FROM ANYWHERE" and press "Confirm"
![mongodb_network_access.png](resources/mongodb_network_access.png)

## Creating a config file
You have to create a `config.toml` in the root directory of this repository like this:

```toml
[bot]

# Bot Token
token = "OaA2MfMzMsgzMTg3MDA5YRE2.trjisg.sI0ds5dX3abh5acbqkLJUQOjseo"

# Whether you want to see more verbose logs.
debug = false

# When you'r ready to release.
# Logs will be larger and last longer in production.
production = true

[logs]

# Default Logging Level
level = "INFO"

# Sentry DSN (optional)
sentry = "https://5636365a78d3344a9b0445536b792440447a@o141345.ingest.sentry.io/4747464"


[database]

# This bot requires a URI from a MongoDB you set up.
uri = "mongodb+srv://argus:password123@argus-alpha.abcd.mongodb.net/argus?retryWrites=true&w=majority"

# Name of the database.
name = "argus"

[global]

# Name of the bot you want rendered.
name = "Argus"

# The Discord Snowflake for the guild the bot is in.
guild_id = 729148350156134416
```
Make sure you replace the token with your bot's token, the uri with the mongodb link you copied and the guild_id with the ID of your discord server in which you want the bot to function (This can be obtained by right clicking your server and pressing "Copy Server ID" after enabling Developer Mode in the Discord settings (Advanced tab))

## Downloading Python

You need to download Python, this has been tested to work with Python 3.11
Download it from: https://www.python.org/downloads/release/python-3119/ (version 3.11.9)

## Downloading Poetry for Python

This project requires the Poetry dependency manager, which can be installed by following the official guide:
https://python-poetry.org/docs/#installing-with-the-official-installer

## Installing the libraries

First, install the project manually using the following terminal command:
```bash
pip install -e .
```

Then, you'll have to install the dependencies with Poetry using:
```bash
poetry install
```

To start the bot simply enter this in the terminal:

```bash
argus
```

Sync commands to the server by sending this in any channel:

```
$sync
```

Finally initialize the server by doing:

```
/setup roles
/setup channels
```

If you server is Level 2 boosted then also do:

```
/setup icons
```

Once the channels, roles and icons are set up, you can enable the debating module with this command:

```
/global enable
```

The rest of the commands are self-explanatory, but you can find the [user manual here](https://wiki.opendebates.net/en/argus/manual).


---
