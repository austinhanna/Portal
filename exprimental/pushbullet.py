from pushbullet import Pushbullet

api_key = o.nucZ1kxbUzWvTe7FC4SzlG9H8TSOuO0x

pb = Pushbullet(api_key)

push = pb.push_note("This is the title", "This is the body")
