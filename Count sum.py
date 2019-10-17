def count_positives_sum_negatives(arr):
    sum_of_positives = sum(1 for x in arr if x > 0)
    sum_of_negatives = sum(x for x in arr if x < 0)
    return [sum_of_positives, sum_of_negatives] if len(arr) else []