import 'package:flutter/material.dart';

import 'package:family/main.dart';
import 'package:family/src/parent/parent_model.dart';
import 'package:family/src/parent/parent_form_provider.dart';
import 'package:family/src/parent/parent_service.dart';
import 'package:family/src/parent/parents_list_screen.dart';

class ParentCard extends StatelessWidget {
  final Parent parent;
  final Function onUpdate;

  const ParentCard({super.key, required this.parent, required this.onUpdate});

  @override
  Widget build(BuildContext context) {
    return Dismissible(
      key: Key(parent.id.toString()),
      direction: DismissDirection.endToStart,
      onDismissed: (direction) {
        if (direction == DismissDirection.endToStart) {
          parentsService.deleteParent(parent);
        }
      },
      background: Container(
        decoration: BoxDecoration(color: Colors.red),
        alignment: Alignment.centerRight,
        padding: EdgeInsets.only(right: 20),
        child: Icon(Icons.delete, color: Colors.white),
      ),
      child: Card(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            IconButton(
              icon: Icon(Icons.edit, size: 18),
              onPressed: () {
                getIt<ParentFormProvider>().setParent(parent);
                Navigator.of(context).pushNamed(
                  ParentsListScreen.routeName, 
                  arguments:{
                    'parent': parent,
                  }
                );
              },
            ),
            Expanded(
              child: Text(parent.name),
            ),
          ],
        ),
      ),
    );
  }
}
