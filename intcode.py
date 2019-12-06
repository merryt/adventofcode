def process_opcode(opcode):
    op_array =  [ int(x) for x in opcode.split(",")]
    loc = 0
    while(op_array[loc] is not 99 ):
        pos_to_alter_1 = op_array[loc + 1]
        pos_to_alter_2 = op_array[loc + 2]
        target_loc= op_array[loc + 3]
        if(op_array[loc] == 1):
            # add
            op_array[target_loc] = op_array[pos_to_alter_1] + op_array[pos_to_alter_2]

        elif(op_array[loc] is 2):
            # miltiply
            op_array[target_loc] = op_array[pos_to_alter_1] * op_array[pos_to_alter_2]

        loc += 4
    return ','.join(str(e) for e in op_array)


def part1(filename):
    part1_data = open(filename,"r")
    op_array =  [ int(x) for x in part1_data.read().split(",")]
    op_array[1] = 12
    op_array[2] = 2
    result = process_opcode(','.join(str(e) for e in op_array))
    return result

def part2(filename):
    part1_data = open(filename,"r")
    op_array =  [ int(x) for x in part1_data.read().split(",")]
    for x in range(0,100):
        op_array[1] = x
        for y in range(0,100):
            op_array[2] = y
            result = process_opcode(','.join(str(e) for e in op_array))
            result_array = [ int(x) for x in result.split(",")]


            if(result_array[0] == 19690720):
                return x,y
    return False

print(part1("prob2_input"))
