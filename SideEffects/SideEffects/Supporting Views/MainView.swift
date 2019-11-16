//
//  MainView.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/15/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import SwiftUI

struct MainView: View {
    @State var isAddPresented = false
    @Environment(\.presentationMode) var presentation
    @State private var searchText = ""
    
    @Binding var networkManager: NetworkManager
    var body: some View {
        Text(/*@START_MENU_TOKEN@*/"Hello, World!"/*@END_MENU_TOKEN@*/)
    }
}

struct MainView_Previews: PreviewProvider {
    static var previews: some View {
        Text("Hello World")
        //MainView()
    }
}
