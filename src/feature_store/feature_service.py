from .feature_registry import FEATURE_REGISTRY


class FeatureService:

    def get_feature(self, name):

        return FEATURE_REGISTRY.get(name)