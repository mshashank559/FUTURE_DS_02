import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (only on first run)
nltk.download('punkt')
nltk.download('stopwords')

# Base English stopwords
_BASE_STOPWORDS = set(stopwords.words('english'))

# Domain‑specific stopwords to filter out chatter
_DOMAIN_STOPWORDS = {
    'im', 'ive', 'please', 'would', 'could', 'also', 
    'thank', 'thanks', 'hello', 'hi', 'regards'
}

ALL_STOPWORDS = _BASE_STOPWORDS.union(_DOMAIN_STOPWORDS)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Keep only letters and spaces
    tokens = word_tokenize(text, preserve_line=True)
    tokens = [tok for tok in tokens if tok not in ALL_STOPWORDS and tok.strip()]
    return " ".join(tokens)
