import graphene

from ..core.types import SortInputObjectType


class WebhooksSortField(graphene.Enum):
    NAME = "name"
    SERVICE_ACCOUNT = "service_account"
    TARGET_URL = "target_url"

    @property
    def description(self):
        # pylint: disable=no-member
        if self in [
            WebhooksSortField.NAME,
            WebhooksSortField.SERVICE_ACCOUNT,
            WebhooksSortField.TARGET_URL,
        ]:
            sort_name = self.name.lower().replace("_", " ")
            return f"Sort webhooks by {sort_name}."
        raise ValueError("Unsupported enum value: %s" % self.value)


class WebhooksSortingInput(SortInputObjectType):
    class Meta:
        sort_enum = WebhooksSortField
        type_name = "webhooks"
