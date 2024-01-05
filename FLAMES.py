def remove_match_char(list1, list2):
    """
    Remove common characters between two lists.

    Parameters:
    - list1: First list of characters.
    - list2: Second list of characters.

    Returns:
    - A tuple containing the concatenated list and a flag indicating whether common characters were found.
    """
    common_found = False

    for char in list1[:]:
        if char in list2:
            common_found = True
            list1.remove(char)
            list2.remove(char)

    result_list = list1 + ["*"] + list2
    return result_list, common_found


def get_cleaned_input(prompt):
    """
    Get user input, convert to lowercase, and remove spaces.

    Parameters:
    - prompt: The prompt for user input.

    Returns:
    - Cleaned input string.
    """
    user_input = input(prompt).lower().replace(" ", "")
    return user_input


if __name__ == "__main__":
    # Take names as input
    player1_name = get_cleaned_input("Player 1 name: ")
    player2_name = get_cleaned_input("Player 2 name: ")

    player1_list = list(player1_name)
    player2_list = list(player2_name)

    proceed = True

    # Keep calling remove_match_char function until common characters are found
    while proceed:
        result_list, common_found = remove_match_char(player1_list, player2_list)
        player1_list = result_list[:result_list.index("*")]
        player2_list = result_list[result_list.index("*") + 1:]
        proceed = common_found

    # Count total remaining characters
    count = len(player1_list) + len(player2_list)

    # List of FLAMES acronym
    result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    # Determine the relationship status
    while len(result) > 1:
        split_index = (count % len(result) - 1 + len(result)) % len(result)
        result = result[split_index + 1:] + result[:split_index]

    # Print the final result
    print("Relationship status:", result[0])
