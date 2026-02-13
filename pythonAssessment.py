"""
Text Analysis Script for News Article
This module provides functions to analyze text content of news articles.
"""

import re
from collections import Counter


# The news article text
NEWS_ARTICLE = """ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the "Apple Pie Master," this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. "This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results," Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, "The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one."

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. "We want to cater to all taste preferences, from the traditional to the adventurous," said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master's environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. "Sustainability is at the core of all our product designs," emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, "It's like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings."

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. "The Apple Pie Master is just the beginning," said CEO Jane Doe. "We're exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking."

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations."""


def count_specific_word(text, word):
    """
    Count the number of occurrences of a specific word in the text.
    
    Args:
        text (str): The string to search through.
        word (str): The search word.
    
    Returns:
        int: The count of occurrences of the word (case-insensitive).
    
    Edge Cases:
        - If no matches are found, returns 0.
    """
    if not text or not word:
        return 0
    
    # Convert to lowercase for case-insensitive matching
    text_lower = text.lower()
    word_lower = word.lower()
    
    # Use word boundary regex for accurate word matching
    pattern = r'\b' + re.escape(word_lower) + r'\b'
    matches = re.findall(pattern, text_lower)
    
    return len(matches)


def identify_most_common_word(text):
    """
    Identify the most common word in the text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        str: The most common word, or None if text is empty.
    
    Edge Cases:
        - An empty string should return None.
    """
    if not text or not text.strip():
        return None
    
    # Extract words (only alphabetic characters)
    words = re.findall(r'[a-zA-Z]+', text.lower())
    
    if not words:
        return None
    
    # Count word occurrences
    word_counts = Counter(words)
    
    # Get the most common word
    most_common = word_counts.most_common(1)
    
    return most_common[0][0] if most_common else None


def calculate_average_word_length(text):
    """
    Calculate the average length of words in the text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        float: The average word length.
    
    Edge Cases:
        - An empty string should return 0.
        - Excludes punctuation marks and special characters.
    """
    if not text or not text.strip():
        return 0.0
    
    # Extract words (only alphabetic characters)
    words = re.findall(r'[a-zA-Z]+', text)
    
    if not words:
        return 0.0
    
    # Calculate total length of all words
    total_length = sum(len(word) for word in words)
    
    # Calculate and return average
    average = total_length / len(words)
    
    return average


def count_paragraphs(text):
    """
    Count the number of paragraphs in the text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        int: The number of paragraphs.
    
    Edge Cases:
        - An empty string should return 1.
        - Paragraphs are defined based on empty lines between blocks of text.
    """
    if not text or not text.strip():
        return 1
    
    # Split by empty lines (one or more newlines)
    paragraphs = re.split(r'\n\s*\n', text.strip())
    
    # Filter out empty paragraphs
    non_empty_paragraphs = [p for p in paragraphs if p.strip()]
    
    return len(non_empty_paragraphs) if non_empty_paragraphs else 1


def count_sentences(text):
    """
    Count the number of sentences in the text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        int: The number of sentences.
    
    Edge Cases:
        - An empty string should return 1.
        - Sentences are defined based on punctuation marks (., !, ?).
    """
    if not text or not text.strip():
        return 1
    
    # Split by sentence-ending punctuation marks
    # This pattern matches periods, exclamation marks, and question marks
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out empty strings
    non_empty_sentences = [s for s in sentences if s.strip()]
    
    return len(non_empty_sentences) if non_empty_sentences else 1


def main():
    """
    Main function to demonstrate all text analysis functions.
    """
    print("=" * 70)
    print("TEXT ANALYSIS RESULTS FOR NEWS ARTICLE")
    print("=" * 70)
    print()
    
    # Display the article
    print("NEWS ARTICLE:")
    print("-" * 70)
    print(NEWS_ARTICLE[:500] + "..." if len(NEWS_ARTICLE) > 500 else NEWS_ARTICLE)
    print("-" * 70)
    print()
    
    # Test count_specific_word with different words
    print("1. COUNT SPECIFIC WORD")
    print("-" * 40)
    test_words = ["Apple", "pie", "ACME", "technology", "baking", "zxyz"]
    for word in test_words:
        count = count_specific_word(NEWS_ARTICLE, word)
        print(f"   Count of '{word}': {count}")
    print()
    
    # Test identify_most_common_word
    print("2. MOST COMMON WORD")
    print("-" * 40)
    most_common = identify_most_common_word(NEWS_ARTICLE)
    print(f"   Most common word: '{most_common}'")
    print()
    
    # Test identify_most_common_word with empty string
    most_common_empty = identify_most_common_word("")
    print(f"   Most common word (empty string): {most_common_empty}")
    print()
    
    # Test calculate_average_word_length
    print("3. AVERAGE WORD LENGTH")
    print("-" * 40)
    avg_length = calculate_average_word_length(NEWS_ARTICLE)
    print(f"   Average word length: {avg_length:.2f}")
    
    avg_length_empty = calculate_average_word_length("")
    print(f"   Average word length (empty string): {avg_length_empty}")
    print()
    
    # Test count_paragraphs
    print("4. COUNT PARAGRAPHS")
    print("-" * 40)
    num_paragraphs = count_paragraphs(NEWS_ARTICLE)
    print(f"   Number of paragraphs: {num_paragraphs}")
    
    num_paragraphs_empty = count_paragraphs("")
    print(f"   Number of paragraphs (empty string): {num_paragraphs_empty}")
    print()
    
    # Test count_sentences
    print("5. COUNT SENTENCES")
    print("-" * 40)
    num_sentences = count_sentences(NEWS_ARTICLE)
    print(f"   Number of sentences: {num_sentences}")
    
    num_sentences_empty = count_sentences("")
    print(f"   Number of sentences (empty string): {num_sentences_empty}")
    print()
    
    # Summary
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"   Total word count (approximate): {len(NEWS_ARTICLE.split())}")
    print(f"   Most common word: '{most_common}'")
    print(f"   Average word length: {avg_length:.2f} characters")
    print(f"   Number of paragraphs: {num_paragraphs}")
    print(f"   Number of sentences: {num_sentences}")
    print("=" * 70)


if __name__ == "__main__":
    main()

