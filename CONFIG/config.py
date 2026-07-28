# Main Configuration
# This file combines all configuration classes into one unified Config class

import os
from CONFIG.commands import CommandsConfig
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.domains import DomainsConfig
from CONFIG.limits import LimitsConfig

def _parse_int_list(env_key, default=""):
    raw = os.environ.get(env_key, default)
    return [int(x.strip()) for x in raw.split(",") if x.strip()]

###########################################################
#        CONFIGURATION LOADED FROM ENVIRONMENT VARIABLES
###########################################################
class Config(object):
    # Bot identity
    BOT_NAME = os.environ.get("BOT_NAME", "tgytdlp_test_bot")
    BOT_NAME_FOR_USERS = os.environ.get("BOT_NAME_FOR_USERS", "tgytdlp_bot")

    # Admins & Groups
    ADMIN = _parse_int_list("ADMIN")
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "@")
    ADMIN_GROUP = _parse_int_list("ADMIN_GROUP")
    ALLOWED_GROUP = _parse_int_list("ALLOWED_GROUP")
    # Restrict private chat usage to these user IDs only (empty list = everyone allowed)
    ALLOWED_USERS = _parse_int_list("ALLOWED_USERS")

    # Telegram credentials
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Mini-app
    MINIAPP_URL = os.environ.get("MINIAPP_URL", "")

    # Log channels
    LOGS_ID = int(os.environ.get("LOGS_ID", 0))
    LOGS_VIDEO_ID = int(os.environ.get("LOGS_VIDEO_ID", 0))
    LOGS_NSFW_ID = int(os.environ.get("LOGS_NSFW_ID", 0))
    LOGS_IMG_ID = int(os.environ.get("LOGS_IMG_ID", 0))
    LOGS_PAID_ID = int(os.environ.get("LOGS_PAID_ID", 0))
    LOG_EXCEPTION = int(os.environ.get("LOG_EXCEPTION", 0))

    # Subscription channel
    SUBSCRIBE_CHANNEL = int(os.environ.get("SUBSCRIBE_CHANNEL", 0))
    SUBSCRIBE_CHANNEL_URL = os.environ.get("SUBSCRIBE_CHANNEL_URL", "")
    # Session string for reading channel admin logs (bots can't read admin logs,
    # so a user session is needed). Generate with: python generate_session_string.py
    CHANNEL_GUARD_SESSION_STRING = os.environ.get("CHANNEL_GUARD_SESSION_STRING", "")

    # Firebase
    USE_FIREBASE = os.environ.get("USE_FIREBASE", "false").lower() == "true"
    BOT_DB_PATH = f"bot/{os.environ.get('BOT_NAME_FOR_USERS', 'tgytdlp_bot')}/"
    VIDEO_CACHE_DB_PATH = "bot/video_cache"
    PLAYLIST_CACHE_DB_PATH = "bot/video_cache/playlists"
    IMAGE_CACHE_DB_PATH = "bot/video_cache/images"
    FIREBASE_USER = os.environ.get("FIREBASE_USER", "")
    FIREBASE_PASSWORD = os.environ.get("FIREBASE_PASSWORD", "")
    FIREBASE_CONF = {
        "apiKey": os.environ.get("FIREBASE_API_KEY", ""),
        "authDomain": os.environ.get("FIREBASE_AUTH_DOMAIN", ""),
        "projectId": os.environ.get("FIREBASE_PROJECT_ID", ""),
        "storageBucket": os.environ.get("FIREBASE_STORAGE_BUCKET", ""),
        "messagingSenderId": os.environ.get("FIREBASE_MESSAGING_SENDER_ID", ""),
        "appId": os.environ.get("FIREBASE_APP_ID", ""),
        "databaseURL": os.environ.get("FIREBASE_DATABASE_URL", ""),
    }

    # Cookies
    # For Docker setup: served by the configuration-webserver container, which shares
    # warp's network namespace — so the bot reaches it at http://localhost/cookies/...
    COOKIE_URL = os.environ.get("COOKIE_URL", "http://localhost/cookies/cookie.txt")
    YOUTUBE_COOKIE_URL = os.environ.get("YOUTUBE_COOKIE_URL", "http://localhost/cookies/youtube.txt")
    YOUTUBE_COOKIE_URL_1 = os.environ.get("YOUTUBE_COOKIE_URL_1", "http://localhost/cookies/youtube-1.txt")
    YOUTUBE_COOKIE_URL_2 = os.environ.get("YOUTUBE_COOKIE_URL_2", "")
    YOUTUBE_COOKIE_URL_3 = os.environ.get("YOUTUBE_COOKIE_URL_3", "")
    YOUTUBE_COOKIE_URL_4 = os.environ.get("YOUTUBE_COOKIE_URL_4", "")
    YOUTUBE_COOKIE_URL_5 = os.environ.get("YOUTUBE_COOKIE_URL_5", "")
    YOUTUBE_COOKIE_URL_6 = os.environ.get("YOUTUBE_COOKIE_URL_6", "")
    YOUTUBE_COOKIE_URL_7 = os.environ.get("YOUTUBE_COOKIE_URL_7", "")
    YOUTUBE_COOKIE_URL_8 = os.environ.get("YOUTUBE_COOKIE_URL_8", "")
    YOUTUBE_COOKIE_URL_9 = os.environ.get("YOUTUBE_COOKIE_URL_9", "")
    YOUTUBE_COOKIE_URL_10 = os.environ.get("YOUTUBE_COOKIE_URL_10", "http://localhost/cookies/youtube-10.txt")
    YOUTUBE_COOKIE_ORDER = os.environ.get("YOUTUBE_COOKIE_ORDER", "round_robin")  # random, round_robin
    YOUTUBE_COOKIE_TEST_URL = os.environ.get("YOUTUBE_COOKIE_TEST_URL", "https://www.youtube.com/watch?v=_GuOjXYl5ew")
    INSTAGRAM_COOKIE_URL = os.environ.get("INSTAGRAM_COOKIE_URL", "http://localhost/cookies/instagram.txt")
    TIKTOK_COOKIE_URL = os.environ.get("TIKTOK_COOKIE_URL", "http://localhost/cookies/tiktok.txt")
    FACEBOOK_COOKIE_URL = os.environ.get("FACEBOOK_COOKIE_URL", "http://localhost/cookies/facebook.txt")
    TWITTER_COOKIE_URL = os.environ.get("TWITTER_COOKIE_URL", "http://localhost/cookies/twitter.txt")
    VK_COOKIE_URL = os.environ.get("VK_COOKIE_URL", "http://localhost/cookies/vk.txt")

    # Internal paths (do not change)
    COOKIE_FILE_PATH = "TXT/cookie.txt"
    PIC_FILE_PATH = "pic.jpg"
    FIREBASE_CACHE_FILE = "dump.json"
    RELOAD_CACHE_EVERY = int(os.environ.get("RELOAD_CACHE_EVERY", 1))  # in hours
    DOWNLOAD_FIREBASE_SCRIPT_PATH = "DATABASE/download_firebase.py"
    AUTO_CACHE_RELOAD_ENABLED = os.environ.get("AUTO_CACHE_RELOAD_ENABLED", "true").lower() == "true"

    # Proxy 1
    PROXY_TYPE = os.environ.get("PROXY_TYPE", "http")  # http, https, socks4, socks5, socks5h
    PROXY_IP = os.environ.get("PROXY_IP", "")
    PROXY_PORT = int(os.environ.get("PROXY_PORT", 3128))
    PROXY_USER = os.environ.get("PROXY_USER", "")
    PROXY_PASSWORD = os.environ.get("PROXY_PASSWORD", "")

    # Proxy 2
    PROXY_2_TYPE = os.environ.get("PROXY_2_TYPE", "socks5")  # http, https, socks4, socks5, socks5h
    PROXY_2_IP = os.environ.get("PROXY_2_IP", "")
    PROXY_2_PORT = int(os.environ.get("PROXY_2_PORT", 3128))
    PROXY_2_USER = os.environ.get("PROXY_2_USER", "")
    PROXY_2_PASSWORD = os.environ.get("PROXY_2_PASSWORD", "")
    PROXY_SELECT = os.environ.get("PROXY_SELECT", "round_robin")  # random, round_robin

    # YouTube PO Token
    YOUTUBE_POT_ENABLED = os.environ.get("YOUTUBE_POT_ENABLED", "true").lower() == "true"
    YOUTUBE_POT_BASE_URL = os.environ.get("YOUTUBE_POT_BASE_URL", "http://localhost:4416")
    YOUTUBE_POT_DISABLE_INNERTUBE = os.environ.get("YOUTUBE_POT_DISABLE_INNERTUBE", "false").lower() == "true"

    # Dashboard
    DASHBOARD_PORT = int(os.environ.get("DASHBOARD_PORT", 5555))
    DASHBOARD_USERNAME = os.environ.get("DASHBOARD_USERNAME", "admin")
    DASHBOARD_PASSWORD = os.environ.get("DASHBOARD_PASSWORD", "admin123")
    ACTIVE_SESSIONS_FILE = "CONFIG/.active_sessions.json"

    STAR_RECEIVER = int(os.environ.get("STAR_RECEIVER", 7360853))

    ###########################################################
    # Below: pulled from sub-configs, no env vars needed
    ###########################################################
    DOWNLOAD_COOKIE_COMMAND = CommandsConfig.DOWNLOAD_COOKIE_COMMAND
    PROXY_COMMAND = CommandsConfig.PROXY_COMMAND
    SUBS_COMMAND = CommandsConfig.SUBS_COMMAND
    CHECK_COOKIE_COMMAND = CommandsConfig.CHECK_COOKIE_COMMAND
    SAVE_AS_COOKIE_COMMAND = CommandsConfig.SAVE_AS_COOKIE_COMMAND
    AUDIO_COMMAND = CommandsConfig.AUDIO_COMMAND
    UNCACHE_COMMAND = CommandsConfig.UNCACHE_COMMAND
    PLAYLIST_COMMAND = CommandsConfig.PLAYLIST_COMMAND
    FORMAT_COMMAND = CommandsConfig.FORMAT_COMMAND
    MEDIINFO_COMMAND = CommandsConfig.MEDIINFO_COMMAND
    SETTINGS_COMMAND = CommandsConfig.SETTINGS_COMMAND
    COOKIES_FROM_BROWSER_COMMAND = CommandsConfig.COOKIES_FROM_BROWSER_COMMAND
    BLOCK_USER_COMMAND = CommandsConfig.BLOCK_USER_COMMAND
    UNBLOCK_USER_COMMAND = CommandsConfig.UNBLOCK_USER_COMMAND
    IGNORE_USER_COMMAND = CommandsConfig.IGNORE_USER_COMMAND
    UNIGNORE_USER_COMMAND = CommandsConfig.UNIGNORE_USER_COMMAND
    BAN_TIME_COMMAND = CommandsConfig.BAN_TIME_COMMAND
    RUN_TIME = CommandsConfig.RUN_TIME
    GET_USER_LOGS_COMMAND = CommandsConfig.GET_USER_LOGS_COMMAND
    CLEAN_COMMAND = CommandsConfig.CLEAN_COMMAND
    USAGE_COMMAND = CommandsConfig.USAGE_COMMAND
    TAGS_COMMAND = CommandsConfig.TAGS_COMMAND
    BROADCAST_MESSAGE = CommandsConfig.BROADCAST_MESSAGE
    GET_USER_DETAILS_COMMAND = CommandsConfig.GET_USER_DETAILS_COMMAND
    SPLIT_COMMAND = CommandsConfig.SPLIT_COMMAND
    RELOAD_CACHE_COMMAND = CommandsConfig.RELOAD_CACHE_COMMAND
    AUTO_CACHE_COMMAND = CommandsConfig.AUTO_CACHE_COMMAND
    SEARCH_COMMAND = CommandsConfig.SEARCH_COMMAND
    KEYBOARD_COMMAND = CommandsConfig.KEYBOARD_COMMAND
    LINK_COMMAND = CommandsConfig.LINK_COMMAND
    IMG_COMMAND = CommandsConfig.IMG_COMMAND
    ADD_BOT_TO_GROUP_COMMAND = CommandsConfig.ADD_BOT_TO_GROUP_COMMAND
    NSFW_COMMAND = CommandsConfig.NSFW_COMMAND
    ARGS_COMMAND = CommandsConfig.ARGS_COMMAND
    LIST_COMMAND = CommandsConfig.LIST_COMMAND

    @classmethod
    def get_messages(cls, user_id=None, language_code=None):
        return safe_get_messages(user_id, language_code)

    @classmethod
    def get_message(cls, message_key, user_id=None, language_code=None):
        messages = cls.get_messages(user_id, language_code)
        return getattr(messages, message_key, f"[{message_key}]")

    # Domains configuration
    GREYLIST = DomainsConfig.GREYLIST
    BLACK_LIST = DomainsConfig.BLACK_LIST
    PORN_DOMAINS_FILE = DomainsConfig.PORN_DOMAINS_FILE
    PORN_KEYWORDS_FILE = DomainsConfig.PORN_KEYWORDS_FILE
    SUPPORTED_SITES_FILE = DomainsConfig.SUPPORTED_SITES_FILE
    UPDATE_PORN_SCRIPT_PATH = DomainsConfig.UPDATE_PORN_SCRIPT_PATH
    WHITELIST = DomainsConfig.WHITELIST
    WHITE_KEYWORDS = getattr(DomainsConfig, "WHITE_KEYWORDS", [])
    NO_COOKIE_DOMAINS = DomainsConfig.NO_COOKIE_DOMAINS
    NO_PROXY_DOMAINS = DomainsConfig.NO_PROXY_DOMAINS
    AUTO_PROXY_DOMAINS = DomainsConfig.AUTO_PROXY_DOMAINS
    PROXY_1_DOMAINS = DomainsConfig.PROXY_1_DOMAINS
    PROXY_2_DOMAINS = DomainsConfig.PROXY_2_DOMAINS
    YTDLP_ONLY_DOMAINS = getattr(DomainsConfig, "YTDLP_ONLY_DOMAINS", [])
    GALLERYDL_ONLY_DOMAINS = getattr(DomainsConfig, "GALLERYDL_ONLY_DOMAINS", [])
    GALLERYDL_ONLY_PATH = getattr(DomainsConfig, "GALLERYDL_ONLY_PATH", [])
    GALLERYDL_FALLBACK_DOMAINS = getattr(DomainsConfig, "GALLERYDL_FALLBACK_DOMAINS", [])
    NO_FILTER_DOMAINS = getattr(DomainsConfig, "NO_FILTER_DOMAINS", [])
    TIKTOK_DOMAINS = DomainsConfig.TIKTOK_DOMAINS
    CLEAN_QUERY = DomainsConfig.CLEAN_QUERY
    PIPED_DOMAIN = DomainsConfig.PIPED_DOMAIN

    # Limits configuration
    MAX_FILE_SIZE_GB = LimitsConfig.MAX_FILE_SIZE_GB
    DOWNLOAD_TIMEOUT = LimitsConfig.DOWNLOAD_TIMEOUT
    MAX_SUB_QUALITY = LimitsConfig.MAX_SUB_QUALITY
    MAX_SUB_DURATION = LimitsConfig.MAX_SUB_DURATION
    MAX_SUB_SIZE = LimitsConfig.MAX_SUB_SIZE
    MAX_PLAYLIST_COUNT = LimitsConfig.MAX_PLAYLIST_COUNT
    MAX_TIKTOK_COUNT = LimitsConfig.MAX_TIKTOK_COUNT
    MAX_VIDEO_DURATION = LimitsConfig.MAX_VIDEO_DURATION
    MAX_IMG_FILES = LimitsConfig.MAX_IMG_FILES
    GROUP_MULTIPLIER = LimitsConfig.GROUP_MULTIPLIER
    NSFW_STAR_COST = LimitsConfig.NSFW_STAR_COST

    # Rate limiting configuration
    RATE_LIMIT_PER_MINUTE = LimitsConfig.RATE_LIMIT_PER_MINUTE
    RATE_LIMIT_PER_HOUR = LimitsConfig.RATE_LIMIT_PER_HOUR
    RATE_LIMIT_PER_DAY = LimitsConfig.RATE_LIMIT_PER_DAY
