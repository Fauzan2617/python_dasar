# operator dictionary

data_dict = {
	"cup":"ucup surucup",
	"tong":"otong surotong",
	"dung":"dudung surudung"
}

data_dict1 = {
	"dwi": "Dwi Putera",
	"putera" : "Putera zan",
	"Fauzan" : "Fauzan Dwi"
}
	


# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

LENDING = len(data_dict1)
print(f"Panjang leng {LENDING}")

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

KEY = "dung"
Check = KEY in data_dict
print(Check)

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan
print(data_dict1.get("fauzan","TIDAK DITEMUKAN"))

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"faqih":"faqihza si kweren"}) # kalau gak ada diadd ajah
print(data_dict)

# mendelete data pada dictionary
del data_dict["faqih"]
print(data_dict)

del data_dict1["dwi"]
print(data_dict1)