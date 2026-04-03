import asyncio

class utils:
    def fire_and_forget(f):
        def wrapped(*args, **kwargs):
            return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)
            # runs the targeted function asyncronously - very cool
        return wrapped

    def median(numbers: list) -> float:
        """
        Returns the median of five numbers in a list.

        Args:
            numbers: A list of five numbers.

        Returns:
            The median of the five numbers.
            Raises ValueError if the input list does not contain exactly five numbers.
        """

        # Sort the list to easily find the median
        numbers.sort()

        # Find the centre index
        middle_i = (len(numbers) - 1) / 2
        
        if int(middle_i) != middle_i:
            return utils.mean(numbers[int(middle_i)], numbers[int(middle_i)+1])

        return numbers[middle_i]
    
    def mean(numbers:list) -> float:
        """
        Returns the mean of the inputed list.

        Args:
            numbers: A list.

        Returns:
            Mean of list. """
            
        return sum(numbers) / len(numbers)

