import numpy as np
import cv2


def toBinary(data):
    # convert `data` to binary format as string
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes):
        return ''.join([ format(i, "08b") for i in data ])
    elif isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")


def encodeData(image, secret_message):
    max_bytes = image.shape[0] * image.shape[1] * 3 // 8

    if len(secret_message) > max_bytes:
        raise ValueError("Gambar terlalu kecil atau pesan terlalu besar")

    secret_message += "#####"

    data_index = 0
    binary_message = toBinary(secret_message)

    data_len = len(binary_message)
    for values in image:
        for pixel in values:
            r, g, b = toBinary(pixel)

            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_message[data_index], 2)
                data_index += 1

            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_message[data_index], 2)
                data_index += 1

            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_message[data_index], 2)
                data_index += 1
                
            if data_index >= data_len:
                break

    return image


def decodeData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = toBinary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]

    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]

    decoded_data = ""
    i = 0
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####":
            break

    data = decoded_data[:-5]
    return data

def encodeImage():
    image_name = input("Enter image name(with extension): ")
    image = cv2.imread(image_name)

    data = input("Masukan text : ")
    if(len(data) == 0):
        raise ValueError('Data is empty')

    encoded_image = encodeData(image, data)
    encoded_image_name = str(image_name.split(".")[0]) + \
        "_encoded." + str(image_name.split(".")[1])
    cv2.imwrite(encoded_image_name, encoded_image)


def decodeImage():
    image_name = input("Enter image name(with extension): ")
    image = cv2.imread(image_name)

    text = decodeData(image)
    return text


def main():
    inMenu = int(input("Program Steganografi\n"
                       "1. Encode\n2. Decode\n3. Exit\nSelect: "))
    isContinue = 1

    if (inMenu == 1):
        encodeImage()

    elif (inMenu == 2):
        print("Pesan Rahasianya Adalah :  " + decodeImage())

    elif(inMenu == 3):
        isContinue = 0
        print("End Program.")

    else:
        raise Exception("Enter correct input")

    return isContinue


if __name__ == '__main__':
    isRun = 1

    while(isRun == 1):
        isRun = main()