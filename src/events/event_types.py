from enum import Enum


class EventType(str, Enum):

    TRANSACTION_CREATED = "transaction_created"

    ENTITY_CREATED = "entity_created"

    ENTITY_UPDATED = "entity_updated"

    FRAUD_SCORE_UPDATED = "fraud_score_updated"

    ALERT_CREATED = "alert_created"

    NEWS_SIGNAL_DETECTED = "news_signal_detected"

    MARKET_SIGNAL_DETECTED = "market_signal_detected"

    NETWORK_PATTERN_DETECTED = "network_pattern_detected"