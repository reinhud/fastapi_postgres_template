import 'package:flutter/material.dart';

import 'package:family/main.dart';
import 'package:family/src/parent/parent_form_provider.dart';

class ParentDetailScreen extends StatefulWidget {
  static const routeName = '/detail';

  const ParentDetailScreen({super.key});

  @override
  State<ParentDetailScreen> createState() => _ParentDetailScreenState();
}

class _ParentDetailScreenState extends State<ParentDetailScreen> {
  final formProvider = getIt<ParentFormProvider>();
  final TextEditingController categoryController = TextEditingController();

  @override
  void initState() {
    super.initState();
    formProvider.addListener((){
      setStateIfMounted(() {});
    });
  }

  void setStateIfMounted(f) {
    if (mounted) setState(f);
  }

  void _handleSave() async {
    if (formProvider.isProcessing) return;
    
    final newItem = await formProvider.saveParent();
    if (newItem != null) {
      print(newItem.name);
      // ignore: use_build_context_synchronously
      Navigator.of(context).pop();
    } else {
      // ToastService.error('Error saving item');
      print('Error saving item');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Parent Details'),
        actions: [
          TextButton(
            onPressed: _handleSave,
            child: Text('Save'),
          )
        ],
      ),
      body: Form(
        key: formProvider.form,
        child: Padding(
          padding: EdgeInsets.all(8.0),
          child: Stack(
            children: [
              Column(
                children: [
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 12.0),
                    child: TextFormField(
                      decoration: InputDecoration(
                        labelText: 'Name',
                      ),
                      autofocus: true,
                      onChanged: formProvider.setName,
                      validator: formProvider.validateName,
                      initialValue: formProvider.parent.name,
                    ),
                  ),
                ],
              ),
              if (formProvider.isProcessing)
                Center(
                  child: CircularProgressIndicator(),
                )
            ],
          ),
        ),
      )
    );
  }
}