'''
Input: an integer
Returns: an integer
'''
def eating_cookies(cookies, noms=None):
    if noms is None:
        noms = {}
    if cookies < 2:
        return 1
    elif cookies == 2:
        return 2
    elif cookies == 3:
        return 4
    elif noms and noms[cookies]:
        return noms[cookies]
    else:
        noms[cookies] = eating_cookies(cookies-1, noms) + eating_cookies(cookies-2, noms) + eating_cookies(cookies-3, noms)

    return noms[cookies]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} noms for Cookie Monster to each {num_cookies} cookies")
