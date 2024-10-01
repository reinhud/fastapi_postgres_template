import 'package:flutter/material.dart';

import 'package:family/src/components/empty_list_indicator.dart';
import 'package:family/src/parent/components/parent_card.dart';
import 'package:family/main.dart';
import 'package:family/src/parent/parents_list_provider.dart';

class ParentsList extends StatefulWidget {
  final Function handleAddParent;
  const ParentsList({super.key, required this.handleAddParent});

  @override
  State<ParentsList> createState() => _ParentsListState();
}

class _ParentsListState extends State<ParentsList> {
  final listProvider = getIt<ParentsListProvider>();

  @override
  void initState() {
    super.initState();

    listProvider.addListener(() {
      setStateIfMounted(() {});
    });
  }

  void setStateIfMounted(f) {
    if (mounted) setState(f);
  }

  Future<void> _refreshData() async {
    await listProvider.fetchItems();
  }


  @override
  Widget build(BuildContext context) {
    final parents = listProvider.parents;

    if (!listProvider.isLoading) {
      return const Center(
        child: CircularProgressIndicator(),
      );
    }
    if (parents.isEmpty) {
      return Center(
        child: EmptyListIndicator(
          buttonText: 'Add Parent',
          onButtonPressed: () {
            widget.handleAddParent();
          },
        ),
      );
    } 
    return RefreshIndicator(
      onRefresh: () => _refreshData(),
      child: ListView.builder(
          itemCount: parents.length,
          itemBuilder: (context, index) {
            final parent = parents.elementAt(index);
            return ParentCard(
              parent: parent, 
              onUpdate: () {
                setState(() {});
              }
            );
          },
        ),
    );
  }
}

