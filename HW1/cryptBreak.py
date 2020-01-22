import sys
from BitVector import *  

def cryptBreak(ciphertextFile,key_bv):
	BLOCKSIZE = 16
	numbytes = BLOCKSIZE // 8
	file = open("cipher.txt","r")
	previous_decrypted_block = file.read().strip()
	encrypted_bv = BitVector( hexstring = previous_decrypted_block )
	print(encrypted_bv)
	for key in range(65536):
		key_bv = BitVector(bitlist = [0]*BLOCKSIZE)
		for i in range(0,len(str(key)) // numbytes):
			keyblock = str(key)[i*numbytes:(i+1)*numbytes]
			key_bv ^= BitVector( textstring = keyblock )
		msg_decrypted_bv = BitVector(size = 0)
		for i in range(0, len(encrypted_bv) // BLOCKSIZE):
			bv = encrypted_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
			temp = bv.deep_copy()
			bv ^=  (previous_decrypted_block)
			previous_decrypted_block = temp
			bv ^=  key_bv
			msg_decrypted_bv += bv
			if "Mark Twain" in msg_decrypted_bv:
				print(key_bv)
				return msg_decrypted_bv 
			else:
				print("noooo")
		 

if __name__ == '__main__':
	final = cryptBreak("hi",2)
	print(final)
