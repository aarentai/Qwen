from datasets import load_dataset
from trl import GRPOConfig, GRPOTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
train_dataset = load_dataset("trl-lib/tldr", split="train")

# Define the reward function, which rewards completions that are close to 20 characters
def reward_len(completions, **kwargs):
    return [-abs(20 - len(completion)) for completion in completions]

# training_args = GRPOConfig(output_dir="/mnt/efs/hcdai/projects/Qwen/trl/output/Qwen2-0.5B-GRPO", logging_steps=10)
training_args = GRPOConfig(output_dir="/mnt/efs/hcdai/projects/Qwen/trl/output/Qwen2-0.5B-GRPO",
                            per_device_train_batch_size=1,
                            gradient_accumulation_steps=8,   # → effective batch = 8
                            fp16=True,                       # keep activations in FP16
                            logging_steps=10,
                            save_steps=250)

trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer, 
    reward_funcs=reward_len,
    args=training_args,
    train_dataset=train_dataset,
)

trainer.train()