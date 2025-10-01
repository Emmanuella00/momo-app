from __future__ import annotations
from typing import Dict, Iterable, List, Optional


def linear_search_by_id(transactions: Iterable[dict], target_id: int) -> Optional[dict]:
    for transaction in transactions:
        if transaction.get("id") == target_id:
            return transaction
    return None


def build_index_by_id(transactions: Iterable[dict]) -> Dict[int, dict]:
    index: Dict[int, dict] = {}
    for transaction in transactions:
        transaction_id = transaction.get("id")
        if transaction_id is not None:
            index[int(transaction_id)] = transaction
    return index


def dict_lookup_by_id(index: Dict[int, dict], target_id: int) -> Optional[dict]:
    return index.get(target_id)


