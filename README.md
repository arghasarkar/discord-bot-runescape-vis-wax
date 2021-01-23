# Discord bot for fetching Runescape's VisWax runes

A discord slash bot for fetching Vis Wax runes for Runescape's D&D. This bot runs on AWS Lambda.

# Using the bot

The bot can be used with the command `/viswax`. 

```text
Sunday the 31st
Slot 1: 
- Air ( mind 28 ) 
Slot 2: 
-  Mist ( air 23, water 19, cosmic 26 )
-  Chaos ( mind26, body27 )
-  Blood ( body 27, death 25 )
```

# Registering the bot
The bot can be registered globally or to a guild. To learn more, please view the Discord documentation [here.](https://discord.com/developers/docs/interactions/slash-commands#authorizing-your-application)
Sample PostMan collection has been provided for registering the bot, fetching commands & deleting commands.

## Creating a new command

Send a **POST** request with JSON payload to https://discord.com/api/v8/applications/{{CLIENT_ID}}/commands

Sample request
```json
{
    "name": "viswax",
    "description": "Gets the Vis wax runes for the day"
}
```

Sample response
```json
{
    "id": "805235581193420821",
    "application_id": "802324286927929344",
    "name": "viswax",
    "description": "Gets the Vis wax runes for the day"
}
```

## Viewing existing commands

Send a **GET** request to https://discord.com/api/v8/applications/{{CLIENT_ID}}/commands

Sample response
```json
[
    {
        "id": "805209896802189392",
        "application_id": "802324286927929344",
        "name": "vis",
        "description": "Gets the Vis wax runes for the day"
    },
    {
        "id": "805235581193420821",
        "application_id": "802324286927929344",
        "name": "viswax",
        "description": "Gets the Vis wax runes for the day"
    }
]
```

## Deleting a command

Send a **DELETE** request to https://discord.com/api/v8/applications/{{CLIENT_ID}}/commands/{{command_id}}

Sample response: 204 (No content)

