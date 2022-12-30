import time
import os
from dotenv import load_dotenv
load_dotenv()

# LOL TOKEN GO BRR
BOT_TOKEN = "o" # your discord bot token
#
MONGO_DB_URL = "mongodb+srv://hacker:chetan2004@cluster0.rxh8r.mongodb.net/?retryWrites=true&w=majority"
OWNERS = [971617059383431199, 908723197862621218, 985097344880082964]  # the bot owners
COOLDOWN_BYPASS = [558861606063308822, 344313283714613248, 679677267164921866, 985097344880082964]  # the users that bypass the cooldown
EPICBOT_GUILD_ID = 984475600993542155  # the id of the epicbot guild
PREMIUM_GUILDS = [984475600993542155, 749996055369875456, 876751925859725332]  # the ids of the premium guilds (it bypasses some cmd requirements)

# AFK KEYS

UD_API_KEY = os.environ.get("UD_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER")
TOP_GG_TOKEN = os.environ.get("SHIT_GG_TOKEN")
TWITCH_CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")
CHAT_BID = os.environ.get("CHAT_BID")
CHAT_API_KEY = os.environ.get("CHAT_API_KEY")
DAGPI_KEY = os.environ.get("DAGPI_KEY")
STATCORD_KEY = "statcord.com-KhPWM7OSJ45t1KFfKGFB"
YOUTUBE_API_KEY = "AIzaSyBLhZYl7JdwhTm9S8YDEKOwg_2AVbxKXtk"

# SECRET LOGS HEHE :3

ONLINE_LOG_CHANNEL = 1001341675601408070
SHARD_LOG_CHANNEL = 1001341675601408070
ADD_REMOVE_LOG_CHANNEL = 1001341675601408070
DATABASE_LOG_CHANNEL = 1001341675601408070
COMMANDS_LOG_CHANNEL = 1001341675601408070
ERROR_LOG_CHANNEL = 1001341675601408070
DM_LOG_CHANNEL = 908723197862621218
BUG_REPORT_CHANNEL = 1001340911311130704
RANK_CARD_SUBMIT_CHANNEL = 1001340820810629210
SUGGESTION_CHANNEL = 1001340820810629210
USER_REPORT_CHANNEL = 1001341570747998228

# WEBHOOK LOGS

WEBHOOKS = {
    "startup": (880847339378573403, os.environ.get("startup_webhook")),
    "add_remove": (880847516537585734, os.environ.get("add_remove_webhook")),
    "cmd_uses": (880847705809760276, os.environ.get("cmd_uses_webhook")),
    "cmd_error": (880846787349446778, os.environ.get("cmd_error_webhook")),
    "event_error": (880844779565506601, os.environ.get("event_error_webhook")),
}

# COLORS

# MAIN_COLOR = 0xDC143C # crimson
MAIN_COLOR = 0x2F3136  # light blue kinda
RED_COLOR = 0x2F3136
ORANGE_COLOR = 0x2F3136
PINK_COLOR = 0x2F3136
PINK_COLOR_2 = 0x2F3136
STARBOARD_COLOR = 0x2F3136
INVISIBLE_COLOR = 0x2F3136

# LINK

WEBSITE_LINK = "https://summrsinv.aahanop.repl.co/"
SUPPORT_SERVER_LINK = "https://discord.gg/Zfz4YKRmSd"
INVITE_BOT_LINK = "https://discord.com/api/oauth2/authorize?client_id=1006762674157277294&permissions=8&scope=bot%20applications.commands"
VOTE_LINK = "https://summrsinv.aahanop.repl.co/"

# ROLES

BOT_MOD_ROLE = 1001342096168456202
OWNER_ROLE = 1001341999447801997
SUPPORTER_ROLE = 1001342321348055110
PARTNER_ROLE = 1001342392361820230
STAFF_ROLE = 1001342428252483644
BOOSTER_ROLE = 1000759250257191052
DESIGN_HELPER_ROLE = 1001342570024140800
VIP_ROLE = 1001342642648518736

# EMOJIS

BADGE_EMOJIS = {
    "normie": "<:members:1001344850806972417>",
    "cutevi": "<:CF_cutie:1001345074904445128>",
    "bot_mod": "<:certifiedmoderator:1001345289317273721>",
    "owner_of_epicness": "<:OWNER:1001345445609615380>",
    "staff_member": "<:DiscordStaffBadge:1001345586265600092>",
    "supporter": "<:EarlySupporter:1001345742784438373>",
    "booster": "<:uc_booster:1001345924565573712>",
    "partner": "<:partnerServer:1001346053196484628>",
    "bug_hunter": "<:BugHunter:1001346197677682758>",
    "elite_bug_hunter": "<:Bughuntergold:1001346324018507886>",
    "early_supporter": "<:early_supporter:1001346456554311680>",
    "Big_PP": "<a:jerk:857215645431103489>",
    "No_PP": "<:ppgone:857198841320964106>",
    "aw||oo||sh": "<a:PetAwish:819234104817877003>",
    "wendo": "<a:MH_wii_clap:857201084727689246>",
    "cat": "<a:CatRainbowJam:857201249447444530>",
    "best_streamer": "<:RamHeart:851480978668781648>",
    "voter": "<:upvote:857205463350116353>",
    "cutie": "<:mmm:834782050006466590>",
    "helper": "<:thanks:800741855805046815>",
    "savior": "🙏",
    "very_good_taste": "<a:petartorol:857212043375280160>",
    "samsung_girl": "<:catgirlboop:857213250512879626>",
    "love_magnet": "<:love_magnet:857215765043347527>",
    "designer": "🎨",
}
EMOJIS = {
    'heawt': '<:Heawt:802801495153967154> ',
    'loading': '<a:Loading:1001327595767484517> ',
    'hacker_pepe': '<a:cdzHackerr:1001477625048477827>  ',
    # 'tick_yes': '<:tickYes:828260365908836423> ',
    'tick_yes': '<:tick:1000260215003942992>',  # '<a:EpicTik:766172079179169813> ',
    # 'tick_no': '<:tickNo:828262032495214643> ',
    'tick_no': '<:error:1000260276622467163>',
    'wave_1': '<a:Flux_wave:1001327676566540408> ',
    'shy_uwu': '<:shy_uwu:836452300179374111> ',
    'add': '<:tick:1000260215003942992> ',
    'remove': '<:error:1000260276622467163> ',
    'pepe_jam': '<a:Pepe_CoronaJam:1001477682032283658> ',
    'pog_stop': '<:PC_PogStop:836870370027503657> ',
    'catjam': '<a:1CatJam:836896091014037555> ',
    'epic_coin': '<a:coinflip_1:1001477744611295333> ',
    'bruh': '<:PogBruh:838345056154812447> ',
    'mmm': '<:mmm:842687641639452673> ',
    'sleepy': '<:CB_sleepy:830641591394893844> ',
    'muted': '<:mute:1001477201809641572> ',
    'unmuted': '<:unmute:1001477516621521009> ',
    'reminder': '⏰ ',
    'cool': '<a:cool:844813588476854273> ',
    'settings': '<a:settings:1001477843181633536> ',
    'settings_color': '<a:settings:1001477843181633536> ',
    'lb': '<a:levelup:1001476560613802036> ',
    'poglep': '<:poglep:836173704249344011> ',
    'weirdchamp': '<:WeirdChamp:851062483090800640> ',
    'twitch': '<:twitch:852475334419021835> ',
    'members': '<:members:853203090001887232> ',
    'ramaziHeart': '<:RamHeart:851480978668781648> ',
    'leveling': '<a:levelup:1001476560613802036> ',
    'vay': '<:vay:849994877629497365> ',
    'chat': '<:Chat:859651327391170591> ',
    'hu_peng': '<:whopingme:861230622525882378> ',
    'disboard': '<:disboard:861565998510637107> ',
    'online': '<:online:1000263368030040074>',
    'idle': '<:status_idle:1000263422186901615>',
    'dnd': '<:dnd:1000263326498033695> ',
    'arrow': '<:arrow:1000738139255607357> ',
    'reaction': '<:add_reaction:873891867610210304> ',
    'cmd_arrow': '<a:im_arrowr:1000737111978299502>  ',
    'youtube': '<a:youtube:1000737888406884374> ',
    'cry_': '<a:cry_:887173073630015508> '
}
EMOJIS_FOR_COGS = {
    'actions': '<:Emo:1000242932131053629>',
    'Setup': '<:Emo:1000242932131053629>',
    'fun': '<:Emo:1000242932131053629>',
    'games': '<:Emo:1000242932131053629>',
    'image': '<:Emo:1000242932131053629>',
    'info': '<:Emo:1000242932131053629>',
    'leveling': '<:Emo:1000242932131053629>',
    'misc': '<:Emo:1000242932131053629>',
    'mod': '<:Emo:1000242932131053629>',
    'music': '<:Emo:1000242932131053629>',
    'nsfw': '<:Emo:1000242932131053629>',
    'config': '<:Emo:1000242932131053629>',
    'starboard': '<:Emo:1000242932131053629>',
    'utility': '<:Emo:1000242932131053629>',
    'user': '<:Emo:1000242932131053629>',
    'notifications': '<:Emo:1000242932131053629>',
    'custom': "<:Emo:1000242932131053629>",
}
CUTE_EMOJIS = [
    "<:shy:844039614032904222>",
    "<:shy_peek:844039614309466134>",
    "<:Shy:851665918236557312>",
    "<:shy2:851666263922966588>",
    "<a:HeartOwO:849179336041168916>",
    "<:Heawt:802801495153967154>",
    "<:UwUlove:836174204108931072>",
    "<:Pikaluv:842981646424473601>",
    "<:mmm:834782050006466590>",
    "<a:kissl:808235261708337182>",
    "<:ur_cute:845151161039716362>",
    "<:thanks:800741855805046815>",
    "<a:hugs:839739273083224104>"
]
THINKING_EMOJI_URLS = [
    'https://cdn.discordapp.com/emojis/862387505852055602.png',
    'https://cdn.discordapp.com/emojis/768302864685727755.png',
    'https://cdn.discordapp.com/emojis/854206416830988318.png',
    'https://cdn.discordapp.com/emojis/853192295277002752.png',
    'https://cdn.discordapp.com/emojis/585956493392871424.png',
    'https://cdn.discordapp.com/emojis/819207595876417546.png'
]

# CREDITS

CREDITS_CONTRIBUTORS = {
    "Mr Potato": ["MrPotato374", "Staff, Supporter, Helper"],
    "ELEXR": ["ELEXR", "Supporter, Helper"],
    "Sengolda": ["Sengolda", "Helper"],
    "QuantumGamerLive": ["QuantumGamerLive", "Helper"],
    "TheUndeadBowman": ["TheUndeadBowman", "Staff, Supporter, Helper"],
    "CAT": ["KittyKart", "Supporter, Helper"],
    "Vishal": ["imkrvishal", "Helper"],
    "Crafterzman": ["Craftzman7", "Helper"],
    "Motzumoto": ["Motzumoto", "Helper"],
    "Windows": ["WindowsCmd", "Helper"],
    "Nek": ["NekWasTaken", "Helper"],
}

# PP

BIG_PP_GANG = [558861606063308822, 344313283714613248, 478623992337530883, 541410668117753876]
NO_PP_GANG = [550083219136053259, 729770314388603020]

# SOME RANDOM STUFF

start_time = time.time()
EMPTY_CHARACTER = "‎"

custom_cmds_tags_lemao = """
**User:**
`{user_name}` - The name of the user.
`{user_nickname}` - The nickname of the user.
`{user_discrim}` - The discriminator of the user.
`{user_tag}` - The complete tag of the user. (Eg. Username#0000)
`{user_id}` - The ID of the user.
`{user_mention}` - The mention of the user.
`{user_avatar}` - The avatar of the user.
**Guild:**
`{guild_name}` - The name of the server.
`{guild_id}` - The ID of the server.
`{guild_membercount}` - The membercount of the server.
`{guild_icon}` - The icon URL of the server.
`{guild_owner_name}` - The name of the owner of the guild.
`{guild_owner_id}` - The ID of the owner of the guild.
`{guild_owner_mention}` - The mention of the owner of the guild.
**Invites:**
`{user_invites}` - The invites of the user.
`{inviter_name}` - The name of the inviter who invited the user.
`{inviter_discrim}` - The discriminator of the inviter.
`{inviter_tag}` - The complete tag of the inviter. (Eg. Username#0000)
`{inviter_id}` - The ID of the inviter.
`{inviter_mention}` - The mention of the inviter.
`{inviter_avatar}` - The avatar of the inviter.
`{inviter_invites}` - The invites of the inviter.
"""

ENABLE = ['enable', 'enabled', 'yes', 'true']
DISABLE = ['disable', 'disabled', 'no', 'false']

DEFAULT_WELCOME_MSG = """
{
    "title": "Welcome",
    "description": "Yay! {user_mention} has joined our server!",
    "color": "MAIN_COLOR",
    "footer": {
        "text": "Invited by {inviter_tag}",
        "icon_url": "{inviter_avatar}"
    },
    "thumbnail": "{user_avatar}"
}
"""
DEFAULT_LEAVE_MSG = """
{
    "title": "Sad!",
    "description": "Sad! **{user_tag}** has left us!",
    "color": "RED_COLOR",
    "footer": {
        "text": "Invited by {inviter_tag}",
        "icon_url": "{inviter_avatar}"
    },
    "thumbnail": "{user_avatar}"
}
"""

DEFAULT_TWITCH_MSG = """
Poggers! **{streamer}** is now live! Go check them out! {url}
"""

DEFAULT_LEVEL_UP_MSG = """
Pog! {user_mention} just leveled up to level {level}!
"""

DEFAULT_AUTOMOD_CONFIG = {
    "banned_words": {
        "enabled": False,
        "words": [],
        "removed_words": []
    },
    "all_caps": {
        "enabled": False
    },
    "duplicate_text": {
        "enabled": False
    },
    "message_spam": {
        "enabled": False
    },
    "invites": {
        "enabled": False
    },
    "links": {
        "enabled": False,
        "whitelist": []
    },
    "mass_mentions": {
        "enabled": False
    },
    "emoji_spam": {
        "enabled": False
    },
    "zalgo_text": {
        "enabled": False
    },

    "ignored_channels": [],
    "allowed_roles": []
}

DEFAULT_BANNED_WORDS = [
    'nigg', 'n1gg', 'n*gg',
    'cunt', 'bitch', 'dick',
    'pussy', 'asshole', 'b1tch',
    'b!tch', 'b*tch', 'blowjob',
    'cock', 'c0ck', 'faggot',
    'whore', 'negro', 'retard',
    'slut', 'rape', 'n i g g '
]

GLOBAL_CHAT_RULES = """
**Global chat rules:**
- No Racism, Sexism, Homophobia or anything stupid.
- No NSFW messages or pictures or emotes.
- Do not be rude to anyone.
- No spamming.
- No self promo.
- No malicious links.
**If your message has a "❌" reaction added, that means your message was not sent because you broke one of these rules.**
**If you break any of these rules, you WILL get blacklisted and won't be able to use the bot.**
If you see anyone breaking these rules please report them using the `report` command.
"""

ANTIHOIST_CHARS = "!@#$%^&*()_+-=.,/?;:[]{}`~\"'\\|<>"