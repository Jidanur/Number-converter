def main():
	#binary_to_dec("10000110")
	#print(dec_to_binary(10)[0])
	#print(dec_fraction_to_binary(0.375)[0])
	
	#dec_to_twos_complement(-2280, 16)
	#twos_complement_to_dec("10010111")
	
	#dec_to_ones_complement(-105, 8)
	#ones_complement_to_dec("10010110")
	
	#decimal_to_ieee(-65.2)
	#binary_ieee_to_decimal("01000010011011001000000000000000")
	#hex_ieee_to_decimal("c4c07800")
	hex_ieee_to_decimal("C2328000")

def binary_to_dec(binary_orig):
    result = 0
    out_powers = []
    for ind, digit in enumerate(reversed(list(binary_orig))):
        if digit == "1":
            power_val = ind
            out_powers += [power_val]
            result += 2 ** power_val
    out_txt = " + ".join(map(lambda x: f"2^{x}", out_powers))
    out_txt += " = " + " + ".join(map(lambda x: f"{2**x}", out_powers))
    return (out_txt, result)
	
def dec_to_binary(dec):
    out_txt = ""
    binary_val = ""
    
    if(dec == 0):
        return ("", "0")
    
    while(dec > 0):
        out_txt += f"{dec}/2 = "
        rem = dec % 2
        dec //= 2
        out_txt += f"{dec} -> {rem} \n"
        binary_val = str(rem) + binary_val
    
    return (out_txt, binary_val)
	
def dec_fraction_to_binary(dec_frac):
    out_str = ""
    res = ""
    while dec_frac != 0:
        out_str += f"{dec_frac} * 2 = {dec_frac*2}, take {int((dec_frac*2)%2)}\n"
        dec_frac *= 2
        if(dec_frac >= 1):
            res += "1"
            dec_frac -= 1
        else:
            res += "0"
    return (out_str, res)
	
def invert_binary(binary_val):
    return "".join(list(map(lambda x: "1" if x == "0" else "0", list(binary_val))))
	
def spaced_out_to_hex(spaced_out_res):
    return "".join(list(map(lambda x: hex(int(x, 2))[2].upper(), spaced_out_res.split(" "))))
	
def dec_to_ones_complement(dec_val, bits):
    is_neg = dec_val < 0
    dec_val = abs(dec_val)
    
    binary_calc = dec_to_binary(int(dec_val))
    print(binary_calc[0][:-1])
    
    binary_val = binary_calc[1]
    while len(binary_val) < bits:
        binary_val = "0" + binary_val
    
    print(f"So the number in binary is {binary_val}")
    
    print()
    
    
    
    print(f"The number is {'negative' if is_neg else 'positive'}")
    if(is_neg):
          binary_val = invert_binary(binary_val)
          print(f"So we have to invert it which makes it: {binary_val}")
    print()
          
    return binary_val
          
def dec_to_twos_complement(dec_val, bits):
    ones_complement = dec_to_ones_complement(dec_val, bits)
    twos_complement = bin(int("0b"+ones_complement,2) + 1)[2:]
    print(f"We now add one to its value which makes it {twos_complement}")
    
	
def twos_complement_to_dec(binary_val):
    print(binary_val)
    binary_val = bin(int("0b"+binary_val,2) - 1)[2:]
    print(f"We subtract one so we get: {binary_val}")
    ones_complement_to_dec(binary_val)
    
def ones_complement_to_dec(binary_val):
    is_neg = binary_val[0] == "1"
    if is_neg:
        print("The first digit is 1 so the number is negative, and we need to invert the binary value")
        binary_val = invert_binary(binary_val)
        print(f"After inverting the binary number we get: {binary_val}")
    
    dec_calculation = binary_to_dec(binary_val)
    
    print(dec_calculation[0], "=", dec_calculation[1])
    
    dec_val = dec_calculation[1]
    
    if is_neg:
        print("Recall that the first bit was 1 so the number is negative")
        dec_val  *= -1
    
    print(f"So the final value is: {dec_val}")
	
def space_out_bin(bin_val):
    out = ""
    for segment_start in range(0, len(bin_val), 4):
        out += bin_val[segment_start:segment_start+4] + " "
    return out[:-1]

sign = lambda x: (1, -1)[x<0]

def dec_to_ieee(dec):
    is_neg = dec < 0
    dec = abs(dec)
    
def hex_ieee_to_decimal(hex_val):
    print(hex_val)
    bin_val = hex_to_bin(hex_val)
    binary_ieee_to_decimal(bin_val)
    
def binary_ieee_to_decimal(bin_val):
    print(space_out_bin(bin_val))
    
    is_neg, exponent_encoded, mantissa = int(bin_val[0]), bin_val[1:9], bin_val[9:]
    
    print(f"{is_neg}\t{space_out_bin(exponent_encoded)}\t{space_out_bin(mantissa)}")
    
    print()
    print("Exponent binary to decimal:")
    print(exponent_encoded)
    
    binary_conv_res = binary_to_dec(exponent_encoded)
    print(f"{binary_conv_res[0]} = {binary_conv_res[1]}")
    
    exponent = binary_conv_res[1] - 127
    exponent_tmp = exponent
    
    print(f"{binary_conv_res[1]} = 127 {('[ -' if exponent_tmp < 0 else '( +') + str(abs(exponent_tmp)) + ' )'}")
    print(f"exponent: {exponent_tmp}")
    print()
          
    binary_whole_nums = "1"
    binary_decimal_nums = mantissa
          
    while(exponent_tmp != 0):
          if(exponent_tmp < 0):
              binary_decimal_nums = "0" + binary_decimal_nums
          elif(exponent_tmp > 0):
              binary_whole_nums += binary_decimal_nums[0]
              binary_decimal_nums = binary_decimal_nums[1:]
              
          
          exponent_tmp += -sign(exponent_tmp)
          
    print(f"So we're calculating 1.{mantissa}*2^({exponent}) = {binary_whole_nums}.{binary_decimal_nums}")
          
    dec_whole_num = binary_to_dec(binary_whole_nums)
          
    print()
    print(f"For the whole part: {dec_whole_num[0]} = {dec_whole_num[1]}")
    print()
          
    binary_decimal_nums_tmp = binary_decimal_nums
    
    fraction_powers = []
    fraction_res = 0
    fraction_ind = 1
    while(len(binary_decimal_nums_tmp) > 0):
          
          if(binary_decimal_nums_tmp[0] == "1"):
              fraction_powers += [fraction_ind]
              fraction_res += 1 / (2 ** fraction_ind)
          
          binary_decimal_nums_tmp = binary_decimal_nums_tmp[1:]
          fraction_ind += 1
        
    fraction_str_part1 = " + ".join(map(lambda x: f"1/(2^{x})",fraction_powers))
    fraction_str_part2 = " + ".join(map(lambda x: f"1/{2**x}",fraction_powers))
    print(f"For the fraction part: {binary_decimal_nums}: {fraction_str_part1} = {fraction_str_part2} = {fraction_res}")
    print()
          
    print(f"Putting the whole and fraction parts two together: {(dec_whole_num[1] + fraction_res)}")
    print()
    print(f"The first digit was {is_neg} so the number is {'negative' if is_neg else 'positive'}")
    if(is_neg):
          print(f"So the final value is: -{(dec_whole_num[1] + fraction_res)}")
    
          
    
    
def decimal_to_ieee(dec_val):
    is_neg = dec_val < 0
    dec_val = abs(dec_val)
    print(dec_val)
    print()
    if(dec_val < 0):
        print("We will ignore the sign and come back to it later")
    print()
    whole_part = int(dec_val // 1)
    decimal_part = dec_val % 1
    
    whole_part_calculations = dec_to_binary(whole_part)
    whole_part_binary = whole_part_calculations[1]
    print(f"For the whole part we have {whole_part}")
    print(f"{whole_part_calculations[0][:-1]}")
    print(f"So {whole_part} in base 10 is {whole_part_binary} in base 2")
    print()
    
    fraction_part_calculations = dec_fraction_to_binary(decimal_part)
    fraction_part_binary = fraction_part_calculations[1]
    print(f"For the decimal part we have {decimal_part}")
    print(fraction_part_calculations[0][:-1])
    print(f"So {decimal_part} in base 10 is 0.{fraction_part_binary} in base 2")
    print()
          
    original_binary_val = whole_part_binary + "." + fraction_part_binary
          
    print(f"Putting the two together: {whole_part}.{str(decimal_part)[2:]} in base 10 is {original_binary_val} in base 2")
          
    exponent = 0
    if whole_part_binary == "0":
        while whole_part_binary == "0":
          whole_part_binary = fraction_part_binary[0]
          fraction_part_binary = fraction_part_binary[1:]
          exponent -= 1
    else:
        while len(whole_part_binary) > 1:
          fraction_part_binary = whole_part_binary[-1] + fraction_part_binary
          whole_part_binary = whole_part_binary[:-1]
          exponent += 1
        
    exponent_binary = dec_to_binary(127+exponent)[1]
          
    print(f"{original_binary_val} = {whole_part_binary}.{fraction_part_binary} * 2^{exponent}")
    print()
    
    print(f"Sign: The number is {'negative' if is_neg else 'positive'} so the first bit in the output would be {int(is_neg)}")
    print(f"exponent: 127 + {exponent} = {127 + exponent} in base 10 which is {exponent_binary} in base 2")
    print(f"mantissa: {fraction_part_binary} which will be padded")
          
    while len(exponent_binary) < 8:
          exponent_binary = "0" + exponent_binary
          
    if len(fraction_part_binary) > 23:
          print("Note that we couldn't do fit all of the calculation inside the 16-bit IEEE so we had to ignore some of the last bits")
          fraction_part_binary = fraction_part_binary[:23]
    elif len(fraction_part_binary) < 23:
        fraction_part_binary += ("0"*(23 - len(fraction_part_binary)))
    print()
    print(f"So putting them all together we get:")
    print(f"{int(is_neg)}\t{space_out_bin(exponent_binary)}\t{space_out_bin(fraction_part_binary)}")
    spaced_out_res = space_out_bin(str(int(is_neg)) + exponent_binary + fraction_part_binary)
    print(spaced_out_res)
    print(spaced_out_to_hex(spaced_out_res))
	
main()
	