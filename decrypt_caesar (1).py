def decrypt_caesar(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

if __name__ == "__main__":
    text = "Wklv lv d whvw phvvdjh iru ghfubswlrq xvlqj wkh Fdhvdu Flskhu dojrulwkp lq wkh ilhog ri frpsxwhu qhwzrunv. lw frqwdlqv pdqb whupv vxfk dv, l3s dgguhvvlqj, vxfq, srvw, vlf, urxwlqj, gdwd sdfnhwv dqg pruh."
    key = 3
    original = decrypt_caesar(text, key)
    print("Decrypted message:")
    print(original)