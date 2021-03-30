from typing import Tuple

from lightning_transformers.core.nlp.huggingface.seq2seq.data import Seq2SeqDataModule
from lightning_transformers.task.nlp.translation.config import TranslationDataConfig


class TranslationDataModule(Seq2SeqDataModule):
    cfg: TranslationDataConfig

    @property
    def source_target_column_names(self) -> Tuple[str, str]:
        return self.cfg.source_language, self.cfg.target_language