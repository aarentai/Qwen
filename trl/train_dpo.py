from datasets import load_dataset
from trl import DPOConfig, DPOTrainer
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
train_dataset = load_dataset("trl-lib/ultrafeedback_binarized", split="train")

training_args = DPOConfig(output_dir="/mnt/efs/hcdai/projects/Qwen/trl/output/Qwen2-0.5B-DPO",
                          per_device_train_batch_size=1,
                          gradient_accumulation_steps=8,   # → effective batch = 8
                          max_length=256,
                          fp16=True,                       # keep activations in FP16
                          logging_steps=10,
                          save_steps=250)

trainer = DPOTrainer(model=model, 
                     args=training_args, 
                     processing_class=tokenizer, 
                     train_dataset=train_dataset)

trainer.train()