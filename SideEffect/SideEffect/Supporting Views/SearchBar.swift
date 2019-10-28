//
//  SearchBar.swift
//  SideEffect
//
//  Created by Kevin Tran on 10/24/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct SearchBarView: View {
    @Binding var text: String
    @Binding var isActiveBar: Bool
    var body: some View {
        HStack(alignment: VerticalAlignment.center, spacing: 0, content: {
            ContainerView(text: $text, isActiveField: $isActiveBar)
 
            Button(action: {
                self.isActiveBar = false
                self.text = ""
            }) {
                Text("Cancel")
            }.padding(EdgeInsets(top: 8, leading: 0, bottom: 8, trailing: isActiveBar ? 16 : -52))
        })
    }
}

struct ContainerView: View {
    @Binding var text: String
    @Binding var isActiveField: Bool
    var body: some View {
        ZStack {
            HStack {
                Image(systemName: "magnifyingglass")
                TextField($text, placeholder: Text("Search photos"), onEditingChanged: { isActive in
                    self.isActiveField == isActive
                })
                if !text.isEmpty {
                    Button(action: {
                        self.text = ""
                    }) {
                        Image(systemName: "multiply.circle")
                    }
                }
            }
        }
    }
}

struct SearchBar_Previews: PreviewProvider {
    static var previews: some View {
        SearchBarView(text: "", isActiveBar: true)
    }
}
