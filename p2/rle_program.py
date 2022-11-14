from console_gfx import ConsoleGfx as cg



def main():
    img_data = []
    # print welcome
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    # display test rainbow defined in the ConsoleGfx class
    cg.display_image(cg.test_rainbow)
    # menu loop
    while True:
        # print menu options
        print("\n\nRLE Menu\n" + "-" * 8)
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data\n")
        # prompt for menu choice
        menu_option = input("Select a Menu Option: ")
        if menu_option == '0':
             quit()
        elif menu_option == '1':
            file_name = input("Enter name of file to load: ")
            img_data = cg.load_file(file_name)
        elif menu_option == '2':
            for i in cg.test_image:
                img_data += [i]
            print("Test image data loaded.")
        elif menu_option == '3':
            rle_string = input("Enter an RLE string to be decoded: ")
            img_data = decode_rle(string_to_rle(rle_string))
        elif menu_option == '4':
            hex_string = input("Enter the hex string holding RLE data: ")
            img_data = decode_rle(string_to_data(hex_string))
        elif menu_option == '5':
            hex_flat_data = input("Enter the hex string holding flat data:\n")
            img_data = [ret_hex_dec_val(i) for i in hex_flat_data]
        elif menu_option == '6':
            print("Displaying image...")
            cg.display_image(img_data)
        elif menu_option == '7':
            print("RLE representation:", to_rle_string(encode_rle(img_data)))
        elif menu_option == '8':
            print("RLE hex values:", to_hex_string(encode_rle(img_data)))
        elif menu_option == '9':
            print("Flat hex values:", to_hex_string(img_data))
        else:
            print("Error! Invalid input.")
            continue

# given a hex value, this will return its decimal value
def ret_hex_dec_val(hex_char):
    hex_chars = "0123456789abcdef"
    return hex_chars.find(hex_char.lower())

# given a list of decimal values, this will return a list of hex values
def to_hex_string(data):
    hex_chars = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    col = ""
    for i in data:
        col += hex_chars[i]
    return col

# for no good reason, here's a function that counts how many times there are consecutive numbers in a list
def count_runs(flat_data):
    cur = flat_data[0]
    runs = 1
    run_iters = 1

    for i in flat_data[1:]:
        if i == cur:
            if run_iters == 15:
                runs += 1
                run_iters = 1
            else:
                run_iters += 1
        else:
            cur = i
            runs += 1
            run_iters = 1
    return runs

# compress data list by representing a run of numbers as two numbers,
# the first being the length and the second being the value
def encode_rle(flat_data):
    cur = flat_data[0]
    run_num = cur
    run_iters = 1
    col = []

    for i in flat_data[1:]:
        if i == cur:
            if run_iters == 15:
                col.extend([run_iters, cur])
                run_iters = 1
            else:
                run_iters += 1
            continue
        else:
            col.extend([run_iters, cur])
            run_iters = 1
        cur = i
    col.extend([run_iters, cur])
    return col

# get the length of the unencoded data
# by adding up the length representors
def get_decoded_length(rle_data):
    sum_runs = 0

    for index, item in enumerate(rle_data):
        if index % 2 == 0:
            sum_runs += item
    return sum_runs

# uncompress rle data into flat data
def decode_rle(rle_data):
    nums = []
    iters = []
    col = []

    for i in range(0, len(rle_data), 2):
        iters = rle_data.pop(0)
        num = rle_data.pop(0)
        col.extend([num] * iters)
    return col

# changes string of hex data into list of decimal values
def string_to_data(data_string):
    hex_chars = "0123456789abcdef"
    ret_index = lambda x : hex_chars.find(x.lower())
    col = []
    for i in data_string:
        col.append(ret_index(i))
    return col

# take a decimal rle list, and turn each number
# pair into a decimal-hex pair, with ':' as a
# delimiter between pairs
def to_rle_string(rle_data):
    col = ""
    for i in range(0, int(len(rle_data)/2)):
        a = rle_data.pop(0)
        b = rle_data.pop(0)
        col += str(a) + to_hex_string([b]) + ":"
    col_trimmed = col[0:-1]
    return col_trimmed

# takes last function and reverses it
def string_to_rle(rle_string):
    col = []
    str_col = ""
    hex_chars = "0123456789abcdef"
    # handy little function that returns the decimal value of a hex number
    ret_index = lambda x : hex_chars.find(x.lower())
    for i in rle_string:
        # i is a member of hex_chars, it's not the delimited, so we continue adding to the collector
        if i in hex_chars:
            str_col += i
        # if it isn't, it's the delimited, and we extend the decimal
        # list with all but the last value in str_col, and then the
        # decimal value of the last character in str_col
        else:
            col.extend([int(str_col[0:-1]),ret_index(str_col[-1])])
            str_col = ""
    # append final value, as it doesn't end with a delimiter
    col.extend([int(str_col[0:-1]),ret_index(str_col[-1])])
    return col

# calls main if rle_program.py is run as a program instead of being imported
if __name__ == '__main__':
    main()
