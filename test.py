from utils.extractor import extract_key_info

sample_text = """
The Right to Information Act allows citizens to request
information from public authorities.
"""

print(extract_key_info(sample_text))