class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
         # STEP 1: Build a weighted graph.
        #
        # Each variable represents a node.
        # Each equation represents two directed edges:
        #
        # a / b = value
        # a -> b has weight value
        # b -> a has weight 1 / value
        #
        # defaultdict(list) automatically creates an empty
        # adjacency list whenever a new variable is encountered.

        graph = defaultdict(list)

        for (numerator, denominator), value in zip(equations, values):

            # Store the forward relationship.
            graph[numerator].append((denominator, value))

            # Store the reverse relationship using the reciprocal.
            graph[denominator].append((numerator, 1.0 / value))

        # STEP 2: Define a helper function to answer one query.
        #
        # DFS will search for a path from the current variable
        # to the target variable.
        #
        # accumulated_product represents the product of all
        # ratios along the path we've followed so far.

        def dfs(current, target, accumulated_product, visited):

            # BASE CASE:
            # If we've reached the target, we've successfully
            # found a chain of equations connecting the variables.
            #
            # The accumulated product is our final division result.
            if current == target:
                return accumulated_product

            # Mark this variable as visited.
            #
            # Without this, the reverse edges could create
            # cycles and cause infinite recursion.
            visited.add(current)

            # Explore every variable directly connected
            # to the current variable.
            for neighbor, weight in graph[current]:

                # Skip variables we've already explored.
                if neighbor in visited:
                    continue

                # Following this edge means we multiply
                # our current product by its ratio.
                new_product = accumulated_product * weight

                # Recursively search from the neighboring variable.
                result = dfs(
                    neighbor,
                    target,
                    new_product,
                    visited
                )

                # If this path successfully reached the target,
                # immediately return the computed ratio.
                if result != -1.0:
                    return result

            # We explored every reachable path without
            # finding the target.
            return -1.0

        # STEP 3: Process each query independently.

        answers = []

        for numerator, denominator in queries:

            # If either variable doesn't exist in the graph,
            # we cannot determine the requested ratio.
            if numerator not in graph or denominator not in graph:
                answers.append(-1.0)
                continue

            # Begin DFS at the numerator.
            #
            # The initial accumulated product is 1.0 because
            # multiplying by 1 doesn't change the result.
            #
            # Each query gets its own visited set because
            # previous queries shouldn't affect future searches.
            result = dfs(
                numerator,
                denominator,
                1.0,
                set()
            )

            answers.append(result)

        return answers