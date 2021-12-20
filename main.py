import itertools
import re
import sys


def find_probability_to_miss_graduation(no_of_days):
    """
    This function gives you details about:
        1. The number of ways to attend classes over N days.
        2. The probability that you will miss your graduation ceremony.
    :param no_of_days: 'N' days
    :return: result: probability that you will miss your graduation ceremony.
    """
    try:
        cerem_miss_count = 0
        consecutive_miss_count = 0
        no_of_invalid_ways = 0

        # 0 --> representing 'absent' as 0
        # 1--> representing 'present' as 1
        ways = (list(i) for i in itertools.product([0, 1], repeat=no_of_days))

        no_of_ways = 2**no_of_days
        print(f"Total no of ways:{no_of_ways}")
        print(f"Total no of ways can attend class if we ignore condition(should not absent "
              f"for 4 consecutive days) : {no_of_ways-1}")
        for way in ways:
            way_str = "".join([str(day) for day in way])
            ceremony_miss = way[-1] == 0
            consective_absent_4_days = True if re.search("0{4}", way_str) else False
            if ceremony_miss:
                cerem_miss_count += 1
            if consective_absent_4_days:
                consecutive_miss_count += 1
            if ceremony_miss or consective_absent_4_days:
                no_of_invalid_ways += 1

        no_of_ways_to_attend_class_with_conditions = no_of_ways-consecutive_miss_count
        no_of_ways_for_not_presenting_ceremony = no_of_invalid_ways - consecutive_miss_count

        print(f"Total no of ways can attend class following condition(should not absent for "
              f"4 consecutive days) : {no_of_ways_to_attend_class_with_conditions}")
        result = f"{no_of_ways_for_not_presenting_ceremony}/" \
                 f"{no_of_ways_to_attend_class_with_conditions}"
        print(f"probability of missing graduation ceremony: {result}")
        return result
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"Exception obj: {exc_obj} Type : {exc_type} at line {exc_tb.tb_lineno}")
        print(e)


if __name__ == "__main__":
    print(f"{'*'*50}    TestCase1    {'*'*50}")
    find_probability_to_miss_graduation(5)
    print(f"{'*' * 50}    TestCase2    {'*' * 50}")
    find_probability_to_miss_graduation(10)