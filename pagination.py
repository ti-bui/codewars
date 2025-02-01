# Question: Implement a solution for pagination.
# Given an array of numbers, and page length, and the page number,
# write a solution that fetches the subset of numbers in the array for the given page number and page length.


# Edge Cases:
# Empty input array of numbers -> numbers <= 0
# Invalid page length -> page_length <= 0
# Invalid page number -> page_number <= 0
# Page number beyond the available pages -> page_number > total pages (use mod to wrap back to valid pages)

def pagination(numbers, page_length, page_number):
    if not numbers or page_length <= 0 or page_number <= 0:
        return []

    start_idx = (page_number - 1) * page_length
    end_idx = start_idx + page_length

    if start_idx >= len(numbers):
        return []

    return numbers[start_idx:end_idx]


numbers = [1, 7, 5, 2, 3, 4, 9, 8]

# Example test case:
#           numbers = [1,7,5,2,3,4,9,8]
#                        p1  p2  p3  p4
# pagination(numbers, 2, 4) -> result: [9,8]
# pagination(numbers, 2, 10) -> result: []

print(pagination(numbers, 2, 10))
