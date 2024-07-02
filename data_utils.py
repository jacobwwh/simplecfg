import os
import json
import re

def read_jsonl(path):
    data=[]
    with open(path,'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def write_jsonl(data,path):
    with open(path,'w') as f:
        for d in data:
            f.write(json.dumps(d)+'\n')


def add_lineno(code):
    """Add line numbers to code."""
    lines=code.split('\n')
    new_code=''
    for i, line in enumerate(lines):
        new_code+=f'{i+1}. {line}\n'
    return new_code


def add_lineno_comment(code,docstring_lines=None):
    """Add line numbers to code as comments."""
    lines=code.split('\n')
    for i in range(len(lines)-1,-1,-1):
        if lines[i]=='':
            lines.pop(i)
        else:
            break
    new_code=''
    if docstring_lines is None:
        for i, line in enumerate(lines):
            if i == len(lines) - 1:
                new_code+=f'{line}  #{i+1}'
            else:
                new_code+=f'{line}  #{i+1}\n'
    else:
        docstart,docend=docstring_lines
        for i, line in enumerate(lines):
            if i>=docstart and i<=docend:
                new_code+=f'{line}\n'
            else:
                if i == len(lines) - 1:
                    new_code+=f'{line}  #{i+1}'
                else:
                    new_code+=f'{line}  #{i+1}\n'
    return new_code


def extract_code_blocks_md(markdown_text):
    """Extract code blocks from markdown-style text"""
    # Define the regex pattern to match code blocks enclosed in triple backticks
    code_block_pattern = re.compile(r'```(?:[a-zA-Z]*)\n(.*?)```', re.DOTALL)
    
    # Use findall to extract all code blocks
    code_blocks = re.findall(code_block_pattern, markdown_text)
    
    return code_blocks
