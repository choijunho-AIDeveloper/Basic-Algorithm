def solution(wallet, bill):
    answer = 0
    minWallet, maxWallet = min(wallet), max(wallet)
    minBill, maxBill = min(bill), max(bill)

    while True:
        if minWallet >= minBill and maxWallet >= maxBill:
            break
        else:
            answer += 1
            bill[bill.index(maxBill)] //= 2
            minWallet, maxWallet = min(wallet), max(wallet)
            minBill, maxBill = min(bill), max(bill)

    return answer