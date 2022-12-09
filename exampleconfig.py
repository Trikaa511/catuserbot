from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 29019566
    API_HASH = "807370808839ffe35114184a8a59a7e9"
    # the name to display in your alive message
    ALIVE_NAME = "Trika"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://ktbvuglo:M7J7xXp3hWQTkW40zHNDkn32xtLeXfxv@babar.db.elephantsql.com/ktbvuglo"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzYBuxtAQXMCN8J0j_oWM2xHfZqlCSX3HxoJdkU8w8DqC7dIlZAnwM0817VGDXKiNEFxwoJzwh1rFw0jogw-czimvWI0pZLsGsRcmNZs6cZUhBNepIUB1RU6vW1t0YlSa1XQ_G29ibd8ZJIg2rpDS3gDzq9thPL0VSjVz15FaAcxT_TBreVKO-b-cX98k53Qn1GHnSO7HLGlkh-mV5hcHwfJ308oz575bb9n7qcaWpvlaaN_EIlrViK3lbyq9EuF7WtsWoJkdzk4Fq6mAN4kAZFb8qqU59idNFvQuPFQiv6_g_03Ws5GizFL-vF_zlvQELi8EGAeMSC_TOMKxhl5UMth3Pw="
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
