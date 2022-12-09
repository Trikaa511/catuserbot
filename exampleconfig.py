from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 19720815
    API_HASH = "a82337b061ed245bd80214260993daa6"
    # the name to display in your alive message
    ALIVE_NAME = "Trika"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://ktbvuglo:M7J7xXp3hWQTkW40zHNDkn32xtLeXfxv@babar.db.elephantsql.com/ktbvuglo"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzMBu3x0DEKeN1yKa1Jv8zsO9P0oSgbHAyHpVj5qS53ffBGrNGb-NbD4F_cbIdDfBFrVdZqbDZa7obg-TG-g3rvg2DGP735GEeNLH3H0iiccZyKSs6vPUZIHkhM53cN9IlQDMhNas_LqXrVsLJJzMLbheBFe0udUzXhZ1y71o-n3iAYoxASFJlG1TUh9gAoN7q_IB6re0fwhEfHNWS-bmak4iWZQLYGL79RFQKnYZAE36O3ZxO8jnTO9Qi56f_edc7DcLlZKRww-25Y1nvEwb5yvyxB8shbChTJJRESEE6-WCGoS9fIKOiGMzb8KMwrfsk8oKf14I8afV_ItssB8lAdHDK8="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5978589253:AAGxC6KzgI4RkuwyboUfIsX6CUU4V3Tu-IY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -895907806
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
