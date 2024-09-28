from __future__ import annotations
from enum import Enum
from typing import Dict, Any, List, Optional
from pydantic import BaseModel


class Mode(Enum):
    DETECTIVE = 'DETECTIVE'
    PROACTIVE = 'PROACTIVE'


class ConfigRuleState(Enum):
    ACTIVE = 'ACTIVE'
    DELETING = 'DELETING'
    DELETING_RESULTS = 'DELETING_RESULTS'
    EVALUATING = 'EVALUATING'


class MaximumExecutionFrequency(Enum):
    ONE__HOUR = 'One_Hour'
    THREE__HOURS = 'Three_Hours'
    SIX__HOURS = 'Six_Hours'
    TWELVE__HOURS = 'Twelve_Hours'
    TWENTY_FOUR__HOURS = 'TwentyFour_Hours'


class MaximumExecutionFrequency(Enum):
    ONE__HOUR = 'One_Hour'
    THREE__HOURS = 'Three_Hours'
    SIX__HOURS = 'Six_Hours'
    TWELVE__HOURS = 'Twelve_Hours'
    TWENTY_FOUR__HOURS = 'TwentyFour_Hours'


class MessageType(Enum):
    CONFIGURATION_ITEM_CHANGE_NOTIFICATION = (
        'ConfigurationItemChangeNotification')
    CONFIGURATION_SNAPSHOT_DELIVERY_COMPLETED = (
        'ConfigurationSnapshotDeliveryCompleted')
    SCHEDULED_NOTIFICATION = 'ScheduledNotification'
    OVERSIZED_CONFIGURATION_ITEM_CHANGE_NOTIFICATION = (
        'OversizedConfigurationItemChangeNotification')


class Owner(Enum):
    CUSTOM_LAMBDA = 'CUSTOM_LAMBDA'
    AWS = 'AWS'
    CUSTOM_POLICY = 'CUSTOM_POLICY'


class BaseResponse(BaseModel):

    def __init__(self, **data: Dict[str, Any]):
        fields = self.model_fields.keys()
        init_data = {field: data.get(field, None) for field in fields}
        super().__init__(**init_data)


class Scope(BaseResponse):
    ComplianceResourceTypes: Optional[List[str]]
    TagKey: Optional[str]
    TagValue: Optional[str]
    ComplianceResourceId: Optional[str]


class SourceDetail(BaseResponse):
    EventSource: Optional[str]
    MessageType: Optional[MessageType]
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequency]


class CustomPolicyDetails(BaseResponse):
    PolicyRuntime: Optional[str]
    PolicyText: Optional[str]
    EnableDebugLogDelivery: Optional[bool]


class Source(BaseResponse):
    Owner: Optional[Owner]
    SourceIdentifier: Optional[str]
    SourceDetails: Optional[List[SourceDetail]]
    CustomPolicyDetails: Optional[CustomPolicyDetails]


class EvaluationMode(BaseResponse):
    Mode: Optional[Mode]


class ConfigRule(BaseResponse):
    ConfigRuleName: Optional[str]
    ConfigRuleArn: Optional[str]
    ConfigRuleId: Optional[str]
    Description: Optional[str]
    Scope: Optional[Scope]
    Source: Optional[Source]
    InputParameters: Optional[str]
    MaximumExecutionFrequency: Optional[MaximumExecutionFrequency]
    ConfigRuleState: Optional[ConfigRuleState]
    CreatedBy: Optional[str]
    EvaluationModes: Optional[List[EvaluationMode]]


class DescribeConfigRulesResponse(BaseResponse):
    ConfigRules: Optional[List[ConfigRule]]
    NextToken: Optional[str]
