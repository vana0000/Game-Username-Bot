from get_profile import get_player_by_ign

def test_usernames():
    usernames = ["abide", "abode", "about"
]    
    
    for username in usernames:
        result = get_player_by_ign(username)
        print(result)

if __name__ == "__main__":
    test_usernames()
