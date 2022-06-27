# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that
# can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
# Constraints:
#
# 1 <= s.length <= 2000
# s consists of lowercase and / or uppercase English letters only.

def longestPalindrome(s: str) -> int:
    char_dict = {}
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    odd_exists = False
    longest_length = 0
    for value in char_dict.values():
        if value % 2 == 0:
            longest_length += value
        else:
            odd_exists = True
            if value > 1:
                longest_length += (value - 1)

    return (longest_length + 1) if odd_exists else longest_length



def test_longestPalindrome():
    assert longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareq"
                             "metonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingp"
                             "laceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatwe"
                             "shoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundTh"
                             "ebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetra"
                             "ctTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidh"
                             "ereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehav"
                             "ethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeust"
                             "hatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeas"
                             "ureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsd"
                             "erGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshalln"
                             "otperishfromtheearth") == 983
