from __future__ import annotations

import os
import random
import statistics
import time
from typing import List

from api.app import parse_sms_xml
from dsa.search import (
    build_index_by_id,
    dict_lookup_by_id,
    linear_search_by_id,
)


def time_call(callable_fn, *args, repeats: int = 1):
    durations: List[float] = []
    for _ in range(repeats):
        start = time.perf_counter()
        callable_fn(*args)
        end = time.perf_counter()
        durations.append(end - start)
    return {
        "min": min(durations),
        "max": max(durations),
        "avg": statistics.fmean(durations),
        "runs": repeats,
    }


def main():
    repo_root = os.path.dirname(os.path.dirname(__file__))
    xml_path = os.path.join(repo_root, "api", "modified_sms_v2.xml")

    transactions = parse_sms_xml(xml_path)
    if len(transactions) < 20:
        raise SystemExit("Need at least 20 transactions for a meaningful comparison.")

    ids = [t["id"] for t in transactions]
    sample_ids = random.sample(ids, k=min(20, len(ids)))

    index = build_index_by_id(transactions)

    _ = linear_search_by_id(transactions, sample_ids[0])
    _ = dict_lookup_by_id(index, sample_ids[0])

    linear_times: List[float] = []
    dict_times: List[float] = []

    repeats = 100
    for target_id in sample_ids:
        linear_result = time_call(linear_search_by_id, transactions, target_id, repeats=repeats)
        dict_result = time_call(dict_lookup_by_id, index, target_id, repeats=repeats)
        linear_times.append(linear_result["avg"]) 
        dict_times.append(dict_result["avg"]) 

    print("Lookups per id (avg over", repeats, "runs):")
    print(f"Linear search avg: {statistics.fmean(linear_times):.8f} sec")
    print(f"Dict lookup  avg: {statistics.fmean(dict_times):.8f} sec")
    print()
    print("Why is dict faster? Average-case O(1) hashing vs O(n) scan.")
    print("Alternative structures: B-tree/skip list for ordered searches; Trie for prefix keys.")


if __name__ == "__main__":
    main()


