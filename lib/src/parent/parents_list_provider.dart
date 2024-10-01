import 'package:flutter/material.dart';

import 'package:family/src/parent/parent_model.dart';
import 'package:family/src/parent/parent_service.dart';

abstract class ParentsListProvider extends ChangeNotifier {
  bool isLoading = true;
  List<Parent> _parents = [];

  // Getters
  List<Parent> get parents;

  // Operations
  Future<void> fetchItems();
  void setItems(List<Parent> parents);
}

class ParentsListProviderImpl extends ParentsListProvider {
  ParentsListProviderImpl(){
    _init();
  }

  Future<void> _init() async {
    await fetchItems();
  }

  @override
  Future<void> fetchItems() async {
    isLoading = false;
    setItems([]);
    final parents = await parentsService.list();
    setItems(parents);
    isLoading = true;
    notifyListeners();
  }

  @override
  List<Parent> get parents => _parents;

  @override
  void setItems(List<Parent> parents) {
    _parents = parents;
    notifyListeners();
  }
}