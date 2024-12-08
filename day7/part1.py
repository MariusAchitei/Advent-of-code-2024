import itertools
import operator as op
from functools import reduce

inputs = list()


def process_operation2(result, terms):

    operations = list()
    for i, term in enumerate(reversed(terms)):
        if term == 1 and i != 0:
            if process_operation2(result - 1, terms[:i - 1]):
                operations.append("+")
                result -= 1
            elif process_operation2(result, terms[:i - 1]):
                operations.append("*")
        elif result % term == 0:
            # result /= term
            if process_operation2(result / term, terms[:i - 1]):
                operations.append("*")
                result /= term
            elif process_operation2(result - term, terms[:i - 1]):
                operations.append("+")
                result -= term
        else:
            result -= term
            operations.append("+")
    if len(operations) == 0:
        return True
    last_operation = operations.pop()
    return (last_operation == "*" and result == 1) or (last_operation == "+" and result == 0)

def process_operation(result, terms):
    for v in itertools.product([op.add, op.mul], repeat=len(terms) - 1):
        r = reduce(lambda m, i: i[0](m, i[1]), zip(v, terms[1:]), terms[0])
        if result == r:
            return result

def main():
    sum = 0
    rezults = {}
    input_file = open("input.txt", "r")
    for line in input_file:
        result, terms = line.split(":")
        terms = [int(term.strip()) for term in terms.split(" ") if term != ""]
        inputs.append((int(result), terms))

    for result, terms in inputs:
        # if not process_operation2(result, terms) and process_operation(result, terms):
        if process_operation2(result, terms):
            print(f"{result}: {" ".join([str(term) for term in terms])}")
            # print(result, terms)
            rezults["result"] = terms
            sum+=result

    mistakes = []

    # for result, terms in inputs:
    #     if process_operation(result, terms):
    #         sum += result
    #         # print(result, terms)
    #         if result not in rezults:
    #             mistakes.append(f"{result}: {" ".join([str(term) for term in terms])}")
    #             print(f"{result}: {" ".join([str(term) for term in terms])}")

    print(sum)
main()