import 'package:flutter/material.dart';

class EmptyListIndicator extends StatelessWidget {
  final String message;
  final String? buttonText;
  final IconData buttonIcon;
  final VoidCallback? onButtonPressed;

  const EmptyListIndicator({
    super.key,
    this.message = 'No items found',
    this.buttonText,
    this.buttonIcon = Icons.add,
    this.onButtonPressed,
  });

  @override
  Widget build(BuildContext context) {
    final hasButton = buttonText != null && onButtonPressed != null;

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(Icons.info, color: Colors.amber, size: 48),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(message),
        ),
        if (hasButton)
          ElevatedButton.icon(
            onPressed: () => onButtonPressed!(),
            icon: Icon(buttonIcon),
            label: Text(buttonText!),
          ),
      ],
    );
  }
}