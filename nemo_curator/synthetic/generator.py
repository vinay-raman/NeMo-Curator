# Copyright (c) 2024, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
from abc import ABC, abstractmethod
from typing import Any, List, Union

from omegaconf import DictConfig

from nemo_curator import OpenAIClient
from nemo_curator.datasets import DocumentDataset
from nemo_curator.filters.doc_filter import DocumentFilter
from nemo_curator.synthetic import NemotronGenerator
from nemo_curator.utils.module_utils import is_batched


class SyntheticDataGenerator(ABC):
    """
    An abstract base class for synthetic data generator pipeline.

    This class serves as a template for creating specific synethtic
    data generation pipelines.
    """

    def __init__(self):
        super().__init__()
        self._name = self.__class__.__name__

    @abstractmethod
    def generate(self, input_: Union[str, List[str]]) -> Union[str, List[str]]:
        pass

    @abstractmethod
    def parse_response(self, llm_response: Union[str, List[str]]) -> Any:
        pass

    # @abstractmethod
    # def run(self, dataset: DocumentDataset) -> DocumentDataset:
    #     pass