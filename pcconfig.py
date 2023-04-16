import pynecone as pc

config = pc.Config(
    app_name="Card_Counter",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
