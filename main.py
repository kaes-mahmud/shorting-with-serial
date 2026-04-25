import os
import shutil
import re

# ১. ম্যাপ তৈরি করা (আপনার বর্ণনা অনুযায়ী)
NUMBERS = "0123456789"                  # ১০টি
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # ২৬টি
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"  # ২৬টি

# মোট ৬২টি অক্ষরের লিস্ট
MAPPING = list(NUMBERS) + list(UPPERCASE) + list(LOWERCASE)

INPUT_DIR = 'uploads'
OUTPUT_DIR = 'sorted_output'

def natural_key(string_):
    """char_1, char_2, char_10 কে ক্রমানুসারে সাজানোর জন্য"""
    return [int(c) if c.isdigit() else c for c in re.split('([0-9]+)', string_)]

def sort_images_by_name_only():
    # পুরোনো সর্টেড আউটপুট মুছে নতুন করে শুরু করা
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)

    # ২. আউটপুট ফোল্ডার তৈরি
    for i, char in enumerate(MAPPING):
        # Mac/Windows এর জন্য ছোট হাতের ফোল্ডারে _small যোগ করা হচ্ছে
        folder_name = char if i < 36 else f"{char}_small"
        os.makedirs(os.path.join(OUTPUT_DIR, folder_name), exist_ok=True)

    print("🚀 সিরিয়াল অনুযায়ী সর্টিং শুরু হচ্ছে... (AI ব্যবহার করা হচ্ছে না)")

    # ৩. প্রতিটি ফোল্ডারের ভেতর ঢোকা
    folders = [d for d in os.listdir(INPUT_DIR) if os.path.isdir(os.path.join(INPUT_DIR, d))]
    
    for person_folder in folders:
        person_path = os.path.join(INPUT_DIR, person_folder)
        
        # ফাইলগুলো নিয়ে সেগুলোকে নাম অনুযায়ী সাজানো (char_1, char_2... char_63)
        files = [f for f in os.listdir(person_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        files.sort(key=natural_key) 

        print(f"📂 ফোল্ডার {person_folder}: {len(files)}টি ছবি প্রসেস হচ্ছে...")

        # ৪. ছবিগুলোকে সিরিয়াল অনুযায়ী পাঠানো
        for index, filename in enumerate(files):
            # আমরা শুধু প্রথম ৬২টি ছবি নিবো (ম্যাপ অনুযায়ী), ৬৩ নম্বর ব্ল্যাঙ্ক বাদ যাবে
            if index < len(MAPPING):
                char_found = MAPPING[index]
                
                # ফোল্ডার সিলেকশন
                target_folder = char_found if index < 36 else f"{char_found}_small"
                
                src_path = os.path.join(person_path, filename)
                new_name = f"{person_folder}_{filename}"
                dest_path = os.path.join(OUTPUT_DIR, target_folder, new_name)
                
                shutil.copy(src_path, dest_path)

    print("\n✨ অভিনন্দন কায়েস! এবার সব ছবি আপনার সিরিয়াল অনুযায়ী নিখুঁতভাবে সাজানো হয়েছে।")

if __name__ == "__main__":
    sort_images_by_name_only()