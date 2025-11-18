import re
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

VERSION_PATTERN = re.compile(r'arn:aws:[^:]+:[^:]*:[^:]*:[^:]+:\d+$')

class NoVersionPinnedARN(BaseResourceCheck):
    def __init__(self):
        name = "Ensure ARNs do not contain version pinning"
        id = "CKV_AWS_CUSTOM_001"
        supported_resources = [
            'aws_batch_job_definition',
            'aws_lambda_function',
            'aws_ecs_task_definition',
        ]
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf, entity_type):
        if self._check_for_version_pinned_arn(conf):
            return CheckResult.FAILED
        return CheckResult.PASSED

    def _check_for_version_pinned_arn(self, obj):
        if isinstance(obj, str):
            if VERSION_PATTERN.search(obj):
                return True
        elif isinstance(obj, dict):
            for value in obj.values():
                if self._check_for_version_pinned_arn(value):
                    return True
        elif isinstance(obj, list):
            for item in obj:
                if self._check_for_version_pinned_arn(item):
                    return True
        return False

check = NoVersionPinnedARN()
