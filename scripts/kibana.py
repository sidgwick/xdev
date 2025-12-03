import requests
import json


def query(index):
    url = "https://kibana.native.org/api/console/proxy"

    params = {
        "path": f"/{index}/_search",
        "method": "POST",
    }

    payload = {
        "size": 10,
        "query": {"match": {"content": "ERROR"}},
        "sort": [{"time": {"order": "desc"}}],
    }

    headers = {
        "authorization": "Basic YWRtaW46UVlUQlQ3NTNKbWRkRCYjRw==",
        "content-type": "application/json",
        "kbn-version": "8.11.1",
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        params=params,
        json=payload,
    )

    # print(response.text)
    return json.loads(response.text)


index_list = [
    # "tky-native-cex-monitor-uat-20251130",
    "tky-native-quote-ticker-task-uat-20251130",
    # "tky-native-drop-copy-task-uat-20251130",
    # "tky-native-emergency-stop-task-uat-20251130",
    # "tky-native-cex-monitor-spot-uat-20251130",
    # "tky-native-limit-order-executor-task-uat-20251130",
    # "tky-native-liquidation-price-task-uat-20251130",
    # "tky-native-pmm-signer-uat-20251130",
    # "tky-native-credit-calculator-task-uat-20251130",
    # "tky-native-halo-pricer-library-uat-20251130",
    # "tky-native-hedge-signer-uat-20251130",
    # "sg-host-nginx-ingress-uat-20251130",
    # "tky-native-native-config-uat-20251130",
    # "tky-native-onchain-monitor-task-uat-20251130",
    # "tky-native-order-manager-uat-20251130",
    # "tky-native-orderbook-manager-uat-20251130",
    # "tky-native-wid-get-task-uat-20251130",
    # "tky-native-settlement-task-uat-20251130",
    # "tky-native-native-widget-signer-uat-20251130",
    # "tky-native-position-manager-task-uat-20251130",
    # "tky-native-native-operation-signer-uat-20251130",
    # "tky-native-price-monitor-uat-20251130",
    # "tky-native-token-info-uat-20251130",
    # "tky-native-settlement-uat-20251130",
    # "tky-native-limit-order-uat-20251130",
    # "tky-native-dex-monitor-uat-20251130",
    # "tky-native-risk-manager-uat-20251130",
    # "tky-native-pricer-uat-20251130",
    # "tky-native-stock-monitor-uat-20251130",
    # "tky-native-token-price-task-uat-20251130",
    # "halo-tky-nginx-ingress-uat-20251130",
    # "tky-native-pair-trading-task-uat-20251130",
    # "tky-native-native-api-gateway-uat-20251130",
    # "tky-native-stock-quote-ticker-task-uat-20251130",
    # "tky-native-quote-order-task-uat-20251130",
    # "tky-native-solana-backend-signer-uat-20251130",
    # "tky-nginx-ingress-uat-20251130",
    # "tky-native-inventory-monitor-uat-20251130",
    # "tky-native-cex-position-monitor-uat-20251130",
    # "tky-native-emergency-paused-task-uat-20251130",
    # "tky-native-quote-manager-uat-20251130",
    #
    ###############
    #
    # "tky-native-dex-monitor-prod-20251130",
    # "tky-nginx-ingress-prod-20251130",
    # "tky-native-settlement-prod-20251130",
    # "tky-native-drop-copy-task-prod-20251130",
    # "halo-tky-halo-agg-ob-prod-20251130",
    # "tky-native-v2-stock-monitor-prod-v2-20251130",
    # "tky-native-hedge-listener-task-prod-20251130",
    # "tky-native-trade-risk-manager-task-prod-20251130",
    # "tky-native-stock-hedger-task-prod-20251130",
    # "halo-tky-halo-tgtx-balance-prod-20251130",
    # "tky-native-v2-quote-manager-prod-v2-20251130",
    # "tky-native-inventory-monitor-prod-20251130",
    # "tky-native-wid-get-task-prod-20251130",
    # "tky-native-cowswap-solver-gateway-prod-20251130",
    # "halo-tky-halo-price-prod-20251130",
    # "halo-tky-halo-bn-account-trade-prod-20251130",
    # "tky-native-v2-pricer-prod-v2-20251130",
    # "tky-native-v2-halo-pricer-library-prod-v2-20251130",
    # "tky-native-liquidation-price-task-prod-20251130",
    # "tky-native-check-position-task-prod-20251130",
    # "tky-native-cex-position-monitor-prod-20251130",
    # "tky-native-onchain-monitor-task-prod-20251130",
    # "tky-native-cow-indexer-task-prod-20251130",
    # "tky-native-token-info-prod-20251130",
    # "tky-native-credit-calculator-task-prod-20251130",
    # "tky-native-v2-native-config-prod-v2-20251130",
    # "halo-tky-halo-ok-dex-trade-prod-20251130",
    # "tky-native-risk-manager-prod-20251130",
    # "halo-tky-halo-http-server-prod-20251130",
    # "tky-native-token-price-task-prod-20251130",
    # "tky-native-hedge-signer-prod-20251130",
    # "halo-tky-halo-hft-monitor-prod-20251130",
    # "tky-native-v2-orderbook-manager-prod-v2-20251130",
    # "tky-native-hedge-rw-db-prod-20251130",
    # "tky-native-price-monitor-prod-20251130",
    # "halo-tky-halo-paa-prod-20251130",
    # "tky-native-v2-native-api-gateway-prod-v2-20251130",
    # "tky-native-v2-cex-monitor-prod-v2-20251130",
    # "tky-native-position-manager-task-prod-20251130",
    # "halo-tky-halo-ss-order-list-prod-20251130",
    # "halo-tky-halo-cron-price-prod-20251130",
    # "tky-native-trade-hedger-task-prod-20251130",
    # "tky-native-quote-ticker-analysis-task-prod-20251130",
    # "tky-native-settlement-task-prod-20251130",
    # "tky-native-native-admin-prod-20251130",
    # "tky-native-cowswap-solver-gateway-shadow-prod-20251130",
    # "tky-native-v2-stock-quote-ticker-task-prod-v2-20251130",
    # "halo-tky-halo-pretrade-prod-20251130",
    # "tky-native-v2-cex-monitor-spot-prod-v2-20251130",
    # "tky-native-v2-order-manager-prod-v2-20251130",
    # "halo-tky-halo-hft-prod-20251130",
    # "tky-native-quote-order-task-prod-20251130",
    # "tky-native-cowswap-solver-gateway-staging-prod-20251130",
    # "halo-tky-halo-pnl-monitor-prod-20251130",
    # "tky-native-emergency-paused-task-prod-20251130",
    # "tky-native-v2-quote-ticker-task-prod-v2-20251130",
]

for idx in index_list:
    res = query(idx)
    for line in res["hits"]["hits"]:
        print(idx, line["_source"]["content"])
