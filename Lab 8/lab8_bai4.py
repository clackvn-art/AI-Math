
def gradient_descent_1d(initial_w, learning_rate, epochs):
    if learning_rate <= 0:
        raise ValueError("Learning rate phai lon hon 0.")

    if epochs < 0:
        raise ValueError("Epochs khong duoc am.")

    w = float(initial_w)
    loss_history = []

    for epoch in range(epochs + 1):
        loss = (w - 2) ** 2
        loss_history.append(loss)

        if epoch == epochs:
            break

        gradient = 2 * w - 4
        w = w - learning_rate * gradient

    return w, loss_history


if __name__ == "__main__":
    initial_w = 10.0
    learning_rate = 0.1
    epochs = 20

    optimal_w, loss_history = gradient_descent_1d(
        initial_w, learning_rate, epochs
    )

    print("Trong so cuoi cung:", round(optimal_w, 6))
    print("Loss cuoi cung:", round(loss_history[-1], 8))

    print("\nLich su Loss:")
    for epoch, loss in enumerate(loss_history):
        print(f"Epoch {epoch:2d}: Loss = {loss:.8f}")
