/*
 * Problem: Design a method to find the number of occurrences of any given word in a book.
 * A word is represented as a String and a book is represented as a list of strings.
 * This method will be called multiple times.
*/
HashMap<String, Integer> createDictionary(String[] book) {
        HashMap<String, Integer> dictionary = new HashMap<>();
        for (String word : book) {
            word = word.trim();
            if (!word.equals("")) {
                word = word.toLowerCase();
                if (!dictionary.containsKey(word)) {
                    dictionary.put(word, 1);
                }
                dictionary.put(word, dictionary.get(word) + 1);
            }
        }
        return dictionary;
    }

    int getFrequency(String[] book, String word) {
        HashMap<String, Integer> dictionary = createDictionary(book);
        if (dictionary == null || word == null) return -1;
        word = word.toLowerCase();
        if (dictionary.containsKey(word)) {
            return dictionary.get(word);
        }
        return 0;
    }
